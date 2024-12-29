// parse-mdx.js
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMdx from "remark-mdx";

import fs from "fs";

const filePath = process.argv[2];
const mdxContent = fs.readFileSync(filePath, "utf-8");

const tree = unified().use(remarkParse).use(remarkMdx).parse(mdxContent);

// For demonstration, just converting the AST to JSON
console.log(JSON.stringify(tree, null, 2));
