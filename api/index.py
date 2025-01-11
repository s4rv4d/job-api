from flask import Flask, jsonify, send_file
import requests
from bs4 import BeautifulSoup
import json
import os
import markdown
import subprocess
import re

app = Flask(__name__)

def parse_mdx(file_path):
    result = subprocess.run(
        ["node", "parse-mdx.js", file_path],
        capture_output=True, text=True
    )
    ast_json = result.stdout
    # parse the JSON into a Python dict
    ast_dict = json.loads(ast_json)
    return ast_dict

def token_count(text: str, approximate_divisor=4) -> int:
    """
    Roughly estimates token count by dividing length of the text by `approximate_divisor`.
    Replace this with an actual tokenizer (e.g. tiktoken) if you need more accuracy.
    """
    return len(text) // approximate_divisor

def chunk_dictionary(data, max_keys_per_chunk):
    keys = list(data.keys())
    for i in range(0, len(keys), max_keys_per_chunk):
        chunk = [
            {"key": key, "value": data[key]} for key in keys[i:i + max_keys_per_chunk]
        ]
        yield {"content": chunk}

def split_markdown_by_headings_and_size(content: str, max_tokens: int = 800):
    """
    Splits markdown by second-level headings (`##`) and then further splits by paragraphs if needed
    to ensure each chunk stays within `max_tokens`.
    """
    # 1. Split by second-level headings
    sections = re.split(r'^## ', content, flags=re.MULTILINE)
    sections = [section.strip() for section in sections if section.strip()]

    final_chunks = []

    for section in sections:
        # 2. Further split by double newlines (paragraphs)
        paragraphs = re.split(r'\n\s*\n+', section)
        current_chunk = ""

        for para in paragraphs:
            # If adding this paragraph to the current_chunk would exceed max_tokens, 
            # we push the current chunk and start a new one.
            candidate_text = (current_chunk + "\n\n" + para).strip()
            if token_count(candidate_text) > max_tokens:
                if current_chunk:
                    final_chunks.append({"content": current_chunk.strip()})
                current_chunk = para
            else:
                if not current_chunk:
                    current_chunk = para
                else:
                    current_chunk += "\n\n" + para

        if current_chunk:
            final_chunks.append({"content": current_chunk.strip()})

    return final_chunks

def scrape_job_links():
	url = "https://www.base.org/jobs"
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		job_links = []
		for link in soup.find_all('a', href=True):
			href = link['href']
			if 'for=basejobs' in href:

				job_title = link.parent.find('p', class_='w-full text-xl').text
				print(f"Job Title: {job_title}, Link: {href}")

				job_links.append({"message": {"job_title": job_title, "link": href}})
		return job_links
	else:
		return None
	

@app.route('/cdp-docs', methods=["GET"])
def cdp_docs():
	try:
		MDX_FILE_PATH = "public/combined-cdp-docs.md"

		if not os.path.exists(MDX_FILE_PATH):
			return jsonify({"error": "MDX file not found"}), 404
		
		with open(MDX_FILE_PATH, "r", encoding="utf-8") as file:
			mdx_content = file.read()

		
		# html_content = markdown.markdown(mdx_content)

		# soup = BeautifulSoup(html_content, "html.parser")
		# plain_text = soup.get_text()

		# response_data = {
		# 	"content": plain_text
		# }

		html_content = markdown.markdown(mdx_content)
		soup = BeautifulSoup(html_content, 'html.parser')

		data = {}
		for header in soup.find_all(['h1', 'h2', 'h3']):
			header_text = header.get_text()
			next_sibling = header.find_next_sibling()
			content = next_sibling.get_text() if next_sibling else ''
			data[header_text] = content
		
		chunks = list(chunk_dictionary(data, 15))
		print(len(chunks))
		
		# print(data)
		# print(len(data))


		response_data = {
			"chunks": chunks,
		}

		return jsonify({"response": response_data, "status": 200}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 500
	
@app.route('/base-docs', methods=["GET"])
def base_docs():
	try:
		MDX_FILE_PATH = "public/combined-base-docs.md"

		if not os.path.exists(MDX_FILE_PATH):
			return jsonify({"error": "MD file not found"}), 404
		
		with open(MDX_FILE_PATH, "r", encoding="utf-8") as file:
			mdx_content = file.read()

		# response_data = {
		# 	"content": mdx_content
		# }

		html_content = markdown.markdown(mdx_content)
		soup = BeautifulSoup(html_content, 'html.parser')

		data = {}
		for header in soup.find_all(['h1', 'h2', 'h3']):
			header_text = header.get_text()
			next_sibling = header.find_next_sibling()
			content = next_sibling.get_text() if next_sibling else ''
			data[header_text] = content
		
		chunks = list(chunk_dictionary(data, 15))
		print(len(chunks))
		
		# print(data)
		# print(len(data))


		response_data = {
			"chunks": chunks,
		}

		return jsonify({"response": response_data, "status": 200}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route('/base-learn-docs', methods=["GET"])
def base_learn_docs():
	try:
		MDX_FILE_PATH = "public/combined-base-learn.md"

		if not os.path.exists(MDX_FILE_PATH):
			return jsonify({"error": "MD file not found"}), 404
		
		with open(MDX_FILE_PATH, "r", encoding="utf-8") as file:
			mdx_content = file.read()

		# response_data = {
		# 	"content": mdx_content
		# }

		html_content = markdown.markdown(mdx_content)
		soup = BeautifulSoup(html_content, 'html.parser')

		data = {}
		for header in soup.find_all(['h1', 'h2', 'h3']):
			header_text = header.get_text()
			next_sibling = header.find_next_sibling()
			content = next_sibling.get_text() if next_sibling else ''
			data[header_text] = content
		
		chunks = list(chunk_dictionary(data, 15))
		print(len(chunks))
		
		# print(data)
		# print(len(data))


		response_data = {
			"chunks": chunks,
		}

		return jsonify({"response": response_data, "status": 200}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@app.route('/ock-docs', methods=['GET'])
def ock_docs():
	try:
		MDX_FILE_PATH = "public/combined-ock-docs-0.35.8.md"
		if not os.path.exists(MDX_FILE_PATH):
			return jsonify({"error": "MDX file not found"}), 404

		with open(MDX_FILE_PATH, "r", encoding="utf-8") as file:
			mdx_content = file.read()
		
		# chunks = split_markdown_by_headings_and_size(mdx_content, max_tokens=12000)

		# print(len(chunks))

		html_content = markdown.markdown(mdx_content)
		soup = BeautifulSoup(html_content, 'html.parser')

		data = {}
		for header in soup.find_all(['h1', 'h2', 'h3']):
			header_text = header.get_text()
			next_sibling = header.find_next_sibling()
			content = next_sibling.get_text() if next_sibling else ''
			data[header_text] = content
		
		chunks = list(chunk_dictionary(data, 15))
		print(len(chunks))
		
		# print(data)
		# print(len(data))


		response_data = {
			"chunks": chunks,
		}

		# response_data = {
		# 	"content": data,
		# }

		return jsonify({"response": response_data, "status": 200}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 500


@app.route('/jobs', methods=['GET'])
def get_jobs():
	job_links = scrape_job_links()
	if job_links:
		return jsonify({"response": {"jobs": job_links}, "status": 200}), 200
	else:
		return jsonify({
		    "message": "Failed to fetch job listings", "status": 500
		}), 500

@app.route("/ecosystem-apps", methods=['GET'])
def get_apps():
	with open("public/ecosystem_apps.json", "r", encoding="utf-8") as file:
			mdx_content = json.load(file)
   
	if mdx_content:
		return jsonify({"status": 200, "response": mdx_content}), 200
	else:
		return jsonify({
		    "message": "Failed to fetch job listings", "status": 500
		}), 500

@app.route("/notable_people_on_base", methods=['GET'])
def get_people():
    with open("public/notable_people.json", "r", encoding="utf-8") as file:
        mdx_content = json.load(file)
    
    if mdx_content:
        return jsonify({"status": 200, "response": mdx_content}), 200
    else:
        return jsonify({
			"message": "Failed to fetch job listings", "status": 500
		}), 500

@app.route("/base_tutorials", methods=['GET'])
def get_tutorials():
    with open("public/youtube_content.json", "r", encoding="utf-8") as file:
        mdx_content = json.load(file)
    
    if mdx_content:
        return jsonify({"status": 200, "response": mdx_content}), 200
    else:
        return jsonify({
			"message": "Failed to fetch job listings", "status": 500
		}), 500

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)