
<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-setup-overview/creating-a-project-vid.md -->

---
title: Creating a Project
description: Using Hardhat to start a new project.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='840617485' title='Creating a Project' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-setup-overview/hardhat-overview-vid.md -->

---
title: Overview
description: An introduction to Hardhat
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='844387825' title='Hardhat Overview' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-setup-overview/hardhat-setup-overview-sbs.md -->

---
title: Setup and Overview
description: An overview of hardhat, a smart contract development framework
hide_table_of_contents: false
---

In this article, you'll learn about Hardhat: a development framework to create, test, and deploy smart contracts to Ethereum and other supported EVM chains.

---

## Objectives

By the end of this lesson, you should be able to:

- Install and create a new Hardhat project with Typescript support
- Describe the organization and folder structure of a Hardhat project
- List the use and properties of hardhat.config.ts

---

## Overview

[Hardhat] is a development environment that allows you to develop and test Solidity on your local machine. It includes debugging and unit testing tools, and has an ecosystem of third-party-developed plugins that ease development and deployment.

Among other things, these plugins can help you deploy contracts, see the size of your compiled byte-code, and even see unit test coverage.

## Installing Hardhat and creating a new project

As a pre-requisite to start developing smart contracts with Hardhat, Node.js must be installed.

You can then simply type `npx hardhat init`, which provides a set of options to bootstrap a Hardhat project:

```
888    888                      888 888               888
888    888                      888 888               888
888    888                      888 888               888
8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
888    888 .d888888 888    888  888 888  888 .d888888 888
888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888

👷 Welcome to Hardhat v2.11.2 👷‍

? What do you want to do? …
❯ Create a JavaScript project
  Create a TypeScript project
  Create an empty hardhat.config.js
  Quit
```

You are encouraged to select **Create a TypeScript project**, since it provides you with some benefits such as static typing that can reduce the number of errors during development.

You can then enter 'yes' for the remaining options, which include installing the `@nomicfoundation/hardhat-toolbox` package that contains some of the most used Hardhat plugins.

```
✔ What do you want to do? · Create a TypeScript project
✔ Hardhat project root: · {any location}
✔ Do you want to add a .gitignore? (Y/n) · y
✔ Do you want to install this sample project's dependencies with npm (hardhat @nomicfoundation/hardhat-toolbox)? (Y/n) · y
```

### Anatomy of a Hardhat project

After you complete the previous step, the folder structure looks like the following:

- contracts # contracts will go here
- hardhat.config.ts # configuration file for hardhat
- node_modules # node.js package folder
- package-lock.json # node.js package lock file
- package.json # node.js package file
- scripts # place the scripts here
- test # place the tests here
- tsconfig.json # typescript configuration file

It is also common to save hardhat tasks in a `task` folder.

It is important to mention that all these paths are fully configurable in the `hardhat.config.ts` file. You can specify a different folder for the contracts, such as `src`.

### Configuration

You can configure the Hardhat environment in the `hardhat.config.ts` file.

Since the project uses Typescript, you have the benefit of using static typing.

The following is the default configuration:

```tsx
import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';

const config: HardhatUserConfig = {
  solidity: '0.8.17',
};

export default config;
```

You can configure aspects such as:

- default network
- networks
- solidity
- paths
- mocha

For example:

```tsx
import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';

const config: HardhatUserConfig = {
  defaultNetwork: 'base',
  networks: {
    base_sepolia: {
      url: 'https://sepolia.base.org',
      accounts: ['<private key 1>'],
    },
    sepolia: {
      url: 'https://sepolia.infura.io/v3/<key>',
      accounts: ['<private key 1>', '<private key 2>'],
    },
  },
  solidity: {
    version: '0.8.17',
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  paths: {
    sources: './contracts',
    tests: './test',
    cache: './cache',
    artifacts: './artifacts',
  },
};

export default config;
```

## Compiling smart contracts

At this point, you should have a Hardhat project up and running to start developing smart contracts. You may notice Hardhat includes a sample contract called `Lock.sol`.

To run your first command, enter `npx hardhat compile`, which compiles the smart contracts and generates the correct [artifacts](https://hardhat.org/hardhat-runner/docs/advanced/artifacts) that includes the bytecode and ABI.

After running the `npx hardhat compile` command, you should see a new folder named artifacts. This folder contains each contract name as a folder and a
`{ContractName}.json` file.

---

[Solidity Docs]: https://docs.soliditylang.org/en/v0.8.17/
[Remix Project]: https://remix-project.org/
[Hardhat]: https://hardhat.org/
[Compilation Artifacts]: https://hardhat.org/hardhat-runner/docs/advanced/artifacts



<!-- File: ../web/apps/base-docs/base-learn/docs/writing-to-contracts/useSimulateContract.md -->

---
title: The `useSimulateContract` hook
description: Improve your user experience with the `useSimulateContract` hook.
hide_table_of_contents: false
---

The [`useSimulateContract`] hook simulates and validates a contract interaction without actually sending a transaction to the blockchain. Using it allows you to detect and respond to potential errors before the user tries to send a transaction.

---

## Objectives

By the end of this guide you should be able to:

- Implement wagmi's `useSimulateContract` and `useWriteContract` to send transactions to a smart contract
- Configure the options in `useSimulateContract` and `useWriteContract`
- Call a smart contract function on-demand using the write function from `useWriteContract`, with arguments and a value

---

## Refining the Claim Component

In the previous step-by-step, you used [`useWriteContract`] to set up a hook you can use to call the `claim` function in your smart contract when the user clicks a button. The component works well enough, but it can take a long time for the wallet to pop up, particularly if there is network congestion. You also have no way of responding to a problem with the transaction inputs until after the user tries to initiate a transaction.

### Using `useSimulateContract`

The `useSimulateContract` can be used in partnership with `useWriteContract`. To do so, you set up the transaction parameters in `useSimulateContract`, then use the `data?.request` returned by it as an argument in the call to write to the contract. Modify your `TokenInfo` component to test it:

```tsx
// Bad code for example.  See below for fix.
const {
  data: claimData,
  isFetching: claimIsFetching,
  isError: claimIsError,
} = useSimulateContract({
  address: contractData.address as `0x${string}`,
  abi: contractData.abi,
  functionName: 'claim',
});

useEffect(() => {
  if (claimIsError) {
    alert('Unable to claim'); // TODO: Better error handling
  }
}, [claimIsError]);

// No changes to `useWriteContract`
const { writeContract: claim, isPending: claimIsPending } = useWriteContract();

// Other code...

// Update the call to `claim`
const handleClaimClick = () => {
  claim(claimData?.request);
};
```

You'll also need to update your handler to use the TypeScript pre-check feature, because the claim function will be briefly `undefined`.

```tsx
const handleClaimClick = () => {
  claim(claimData!.request);
};
```

Reload the site and observe that the `alert` is triggered on load if you're signed in with an address that has already claimed tokens. You'll also see that the button is disabled, as though the user had clicked it and a transaction is loading in the wallet.

### Making Adjustments

The reason for this is a subtle difference in how `useWriteContract` and `useSimulateContract` work.

In the last step-by-step, you saw how viem runs a simulation of the transaction when the `write` function is called. `useSimulateContract` eagerly runs this simulation and updates it's variables.

You'll need to make some modifications for it to work. The `claimIsError` variable is being triggered when the data for the call is **simulated**, not when the call has settled. As a result, it immediately generates the error, and triggers the `alert` without requiring the user to click the button.

You can solve this a number of ways, including simply not rendering the button if the user has already claimed. You could also modify the code, and combine it with `isError`, to share this information to the user.

```tsx
const {
  data: claimData,
  isFetching: claimIsFetching,
  isError: claimIsError,
} = useSimulateContract({
  address: contractData.address as `0x${string}`,
  abi: contractData.abi,
  functionName: 'claim',
});

// Deleted `useEffect` for `claimIsError`

const { writeContract: claim, isPending: claimIsPending } = useWriteContract();

// Other code

return (
  <div>
    <p>{claimIsFetching.toString()}</p>
    <p>{'Token Balance: ' + tokenBalance}</p>
    <button disabled={claimIsPending || claimIsError} onClick={handleClaimClick}>
      {claimIsPending ? 'Complete In Wallet' : 'Claim Tokens'}
    </button>
    <p>{claimIsError ? 'Unable to claim tokens.' : 'Claim your tokens!'} </p>
  </div>
);
```

---

## Conclusion

In this step-by-step, you updated your app to use the `useSimulateContract` hook to provide a speedier wallet interaction for your users. You've also learned how you can predict and respond to potential errors without the user needing to attempt to send a transaction. You could use this functionality to let them know a username is already taken, a bid amount is not large enough, or an item is no longer available.

---

[wagmi]: https://wagmi.sh/
[`useWriteContract`]: https://wagmi.sh/react/hooks/useWriteContract
[`useSimulateContract`]: https://wagmi.sh/react/hooks/useSimulateContract



<!-- File: ../web/apps/base-docs/base-learn/docs/writing-to-contracts/useWriteContract.md -->

---
title: The `useWriteContract` hook
description: Write to your smart contracts with the `useWriteContract` hook.
hide_table_of_contents: false
---

The [`useWriteContract`] hook allows you to call your `public` and `external` smart contract functions that write to state and create a permanent modification to the data on chain.

---

## Objectives

By the end of this guide you should be able to:

- Implement wagmi's `useWriteContract` hook to send transactions to a smart contract
- Configure the options in `useWriteContract`
- Display the execution, success, or failure of a function with button state changes, and data display

---

## Sending a Transaction to the Blockchain

:::warning

In this step-by-step, you're going to start with the [`useWriteContract`] hook. You probably won't want to use this method in production. In the next step-by-step, we'll show you the [`useSimulateContract`] hook, how it works with `useWriteContract`, and how you can use it to create a better user experience.

Exploring them separately will highlight the functionality provided by the prepare hook.

:::

:::caution

In this module, you'll extend the onchain app you build in the previous module, [Reading and Displaying Data].

:::

You've built an app that can read from your Simple DAO smart contract, but so far, you've used BaseScan to send transactions that call your write functions. You can use the [`useWriteContract`] hook in a similar way to call those functions directly from your app.

### Setting up the Component

Add a new component called `TokenInfo` to the project, and a state variable for `tokenBalance`.

```tsx
import { useState } from 'react';

export function TokenInfo() {
  const [tokenBalance, setTokenBalance] = useState(0);
}
```

### Reading the Token Balance

You'll need to know how many tokens the user has to be able to make decisions on what UI controls to display, so start by adding a `useReadContract`. You don't have a function for this directly in your contract, but your contract inherits from the [OpenZeppelin ERC20] contract, which has a function called `balanceOf` that takes an address and returns the balance for that address.

You'll need the user's address to use in `args`, which you can conveniently get from the [`useAccount`] hook using the pattern below.

```tsx
const { data: balanceData, queryKey: balanceQueryKey } =
  useReadContract({
    address: contractData.address as `0x${string}`,
    abi: contractData.abi,
    functionName: "balanceOf",
    args: [useAccount().address],
  });

useEffect(() => {
  if (balanceData) {
    setTokenBalance(balanceData as number);
  }
}, [balanceData]);

useEffect(() => {
  queryClient.invalidateQueries({ queryKey: balanceQueryKey });
}, [blockNumber, queryClient]);
```

:::caution

Remember, this is an expensive method to watch for data to change on the blockchain. In this case, a more production-suitable solution might be to call `balanceOf` after the user has done something that might change the balance.

:::

Set the `return` for your component to display this balance to the user:

```tsx
return (
  <div>
    <p>{'Token Balance: ' + tokenBalance}</p>
  </div>
);
```

Then, add the component to your app in `index.tsx`.

```tsx
return (
  <div className={styles.container}>
    <main className={styles.main}>
      <ConnectButton />
      <ConnectionWindow />
      <TokenInfo />
      <IssueList />
    </main>
);
```

Run the app and make sure you see the expected balance displayed on the page.

### Setting up `useWriteContract`

The [`useWriteContract`] hook is configured similarly to the [`useReadContract`] hook, with one important difference. You'll need to decompose the `write` property from the function call. This is a function that you can use to call your smart contract function whenever you'd like!

```tsx
const { writeContract: claim, isPending: claimIsPending } = useWriteContract();
```

Add an event handler function and a button. As with the `useReadContract` hook, you can use `isPending` and other state helpers to adjust your UI. The name of this one is a little misleading. `isPending` will be `true` starting from the moment the transaction gets sent to the user's wallet.

You can use this to nudge them to look to their wallet to complete the transaction. Additionally, add a `useEffect` to watch for an error state.

```tsx
const handleClaimClick = () => {
  claim({
    abi: contractData.abi,
    address: contractData.address as `0x${string}`,
    functionName: 'claim',
  });
};

return (
  <div>
    <p>{'Token Balance: ' + tokenBalance}</p>
    <button disabled={claimIsPending} onClick={handleClaimClick}>
      {claimIsPending ? 'Complete In Wallet' : 'Claim Tokens'}
    </button>
  </div>
);
```

Try it out. Notice that the button text briefly changes without the wallet window popping up if you click the `Claim Tokens` button while connected with a wallet that already owns the tokens. The reason this happens is that viem, which underlies wagmi, runs a simulation of the transaction to estimate gas costs. If that simulation fails, it triggers the fail mechanism immediately, rather than allowing the app to send a bad transaction to the blockchain and cost the user gas for a call doomed to fail. You will fix this in the next tutorial.

In the meantime, you'll need to change to a new wallet or redeploy your contract a couple of times to complete your testing. Do that, and try out the call on a wallet that hasn't claimed any tokens. Notice that the button is disabled and the text now prompts the user to look to their wallet to approve the transaction.

---

## Conclusion

In this step-by-step, you've learned how to use the [`useWriteContract`] hook to call your smart contract functions on demand. You've also tested methods to manage the UI/UX experience for your users, based on the state of the transaction, as well as its success or failure.

---

[wagmi]: https://wagmi.sh/
[`useWriteContract`]: https://wagmi.sh/react/hooks/useWriteContract
[`usePrepareContractWrite`]: https://wagmi.sh/react/prepare-hooks/usePrepareContractWrite
[Reading and Displaying Data]: ../reading-and-displaying-data/useAccount
[`useReadContract`]: https://wagmi.sh/react/hooks/useReadContract
[OpenZeppelin ERC20]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol
[`useAccount`]: https://wagmi.sh/react/hooks/useAccount



<!-- File: ../web/apps/base-docs/base-learn/docs/control-structures/control-structures.md -->

---
title: Control Structures
description: Learn how to control code flow in Solidity.
hide_table_of_contents: false
---

Solidity supports many familiar control structures, but these come with additional restrictions and considerations due to the cost of gas and the necessity of setting a maximum amount of gas that can be spent in a given transaction.

---

## Objectives

By the end of this lesson you should be able to:

- Control code flow with `if`, `else`, `while`, and `for`
- List the unique constraints for control flow in Solidity
- Utilize `require` to write a function that can only be used when a variable is set to `true`
- Write a `revert` statement to abort execution of a function in a specific state
- Utilize `error` to control flow more efficiently than with `require`

---

## Control Structures

Solidity supports the basic conditional and iterative [control structures] found in other curly bracket languages, but it **does not** support more advanced statements such as `switch`, `forEach`, `in`, `of`, etc.

Solidity does support `try`/`catch`, but only for calls to other contracts.

:::caution

[Yul] is an intermediate-level language that can be embedded in Solidity contracts and is documented within the docs for Solidity. Yul **does** contain the `switch` statement, which can confuse search results.

:::

### Conditional Control Structure Examples

The `if`, `else if`, and `else`, statements work as expected. Curly brackets may be omitted for single-line bodies, but we recommend avoiding this as it is less explicit.

```solidity
function ConditionalExample(uint _number) external pure returns (string memory) {
    if(_number == 0) {
        return "The number is zero.";
    } else if(_number % 2 == 0) {
        return "The number is even and greater than zero.";
    } else {
        return "The number is odd and is greater than zero.";
    }
}
```

### Iterative Control Structures

The `while`, `for`, and `do`, keywords function the same as in other languages. You can use `continue` to skip the rest of a loop and start the next iteration. `break` will terminate execution of the loop, and you can use `return` to exit the function and return a value at any point.

:::info

You can use `console.log` by importing `import "hardhat/console.sol";`. Doing so will require you to mark otherwise `pure` contracts as `view`.

:::

```solidity
uint times; // Default value is 0!
for(uint i = 0; i <= times; i++) {
    console.log(i);
}

uint timesWithContinue;
for(uint i = 0; i <= timesWithContinue; i++) {
    if(i % 2 == 1) {
        continue;
    }
    console.log(i);
}

uint timesWithBreak;
for(uint i = 0; i <= timesWithBreak; i++) {
    // Always stop at 7
    if(i == 7) {
        break;
    }
    console.log(i);
}

uint stopAt = 10;
while(stopAt <= 10) {
    console.log(i);
    stopAt++;
}

uint doFor = 10;
do {
    console.log(i);
    doFor++;
} while(doFor <= 10);
```

---

## Error Handling

Solidity contains a set of relatively unique, built-in functions and keywords to handle [errors]. They ensure certain requirements are met, and completely abort all execution of the function and revert any state changes that occurred during function execution. You can use these functions to help protect the security of your contracts and limit their execution.

The approach may seem different than in other environments. If an error occurs partly through a high-stakes transaction such as transferring millions of dollars of tokens, you **do not** want execution to carry on, partially complete, or swallow any errors.

### Revert and Error

The `revert` keyword halts and reverses execution. It must be paired with a custom `error`. Revert should be used to prevent operations that are logically valid, but should not be allowed for business reasons. It is **not** a bug if a `revert` is triggered. Examples where `revert` and `error` would be used to control operations include:

- Allowing only certain senders to access functionality
- Preventing the withdrawal of a deposit before a certain date
- Allowing inputs under certain state conditions and denying them under others

Custom `error`s can be declared without parameters, but they are much more useful if you include them:

```solidity
error OddNumberSubmitted(uint _first, uint _second);
function onlyAddEvenNumbers(uint _first, uint _second) public pure returns (uint) {
    if(_first % 2 != 0 || _second % 2 != 0) {
        revert OddNumberSubmitted(_first, _second);
    }
    return _first + _second;
}
```

When triggered, the `error` provides the values in the parameters provided. This information is very useful when debugging, and/or to transmit information to the front end to share what has happened with the user:

```text
call to HelloWorld.onlyAddEvenNumbers errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Error provided by the contract:
OddNumberSubmitted
Parameters:
{
 "_first": {
  "value": "1"
 },
 "_second": {
  "value": "2"
 }
}
Debug the transaction to get more information.
```

You'll also encounter `revert` used as a function, returning a string error. This legacy pattern has been retained to maintain compatibility with older contracts:

```solidity
function oldRevertAddEvenNumbers(uint _first, uint _second) public pure returns (uint) {
    if(_first % 2 != 0 || _second % 2 != 0) {
        // Legacy use of revert, do not use
        revert("One of the numbers is odd");
    }
    return _first + _second;
}
```

The error provided is less helpful:

```text
call to HelloWorld.oldRevertAddEvenNumbers errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
The reason provided by the contract: "One of the numbers is odd".
Debug the transaction to get more information.
```

### Require

The `require` function is falling out of favor because it uses more gas than the pattern above. You should still become familiar with it because it is present in innumerable contracts, tutorials, and examples.

`require` takes a logical condition and a string error as arguments. It is more gas efficient to separate logical statements if they are not interdependent. In other words, don't use `&&` or `||` in a `require` if you can avoid it.

For example:

```solidity
function requireAddEvenNumbers(uint _first, uint _second) public pure returns (uint) {
    // Legacy pattern, do not use
    require(_first % 2 == 0, "First number is not even");
    require(_second % 2 != 0, "Second number is not even");

    return _first + _second;
}
```

The output error message will be the first one that fails. If you were to submit `1`, and `3` to this function, the error will only contain the first message:

```test
call to HelloWorld.requireAddEvenNumbers errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
The reason provided by the contract: "First number is not even".
Debug the transaction to get more information.
```

### Assert and Panic

The `assert` keyword throws a `panic` error if triggered. A `panic` is the same type of error that is thrown if you try to divide by zero or access an array out-of-bounds. It is used for testing internal errors and should never be triggered by normal operations, even with flawed input. You have a bug that should be resolved if an assert throws an exception:

```solidity
function ProcessEvenNumber(uint _validatedInput) public pure {
    // If assert triggers, input validation has failed.  This should never
    // happen!
    assert(_validatedInput % 2 == 0);
    // Do something...
}
```

The output here isn't as helpful, so you may wish to use one of the patterns above instead.

```text
call to HelloWorld.ProcessEvenNumber errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Note: The called function should be payable if you send value and the value you send should be less than your current balance.
Debug the transaction to get more information.
```

---

## Conclusion

In this lesson, you've learned how to control code flow with standard conditional and iterative operators. You've also learned about the unique keywords Solidity uses to generate errors and reset changes if one of them has been triggered. You've been exposed to both newer and legacy methods of writing errors, and learned the difference between `assert` and `require`.

<!-- Reference Style Links -->

[switch]: https://docs.soliditylang.org/en/v0.8.17/yul.html?#switch
[yul]: https://docs.soliditylang.org/en/v0.8.17/yul.html
[control structures]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html
[errors]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html#error-handling-assert-require-revert-and-exceptions



<!-- File: ../web/apps/base-docs/base-learn/docs/control-structures/loops-vid.md -->

---
title: Loops
description: Explore loops in Solidity.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805353144' title='Loops' />



<!-- File: ../web/apps/base-docs/base-learn/docs/control-structures/standard-control-structures-vid.md -->

---
title: If, Else, and Else If
description: Learn how to control your code.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805353200' title='Standard Control Structures' />



<!-- File: ../web/apps/base-docs/base-learn/docs/control-structures/require-revert-error-vid.md -->

---
title: Require, Revert, and Error
description: Handle errors in Solidity.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805353180' title='Require, Revert, and Error' />



<!-- File: ../web/apps/base-docs/base-learn/docs/control-structures/control-structures-exercise.md -->

---
title: Control Structures Exercise
description: Exercise - Demonstrate your knowledge of control structures.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications:

---

## Contract

Create a single contract called `ControlStructures`. It should not inherit from any other contracts and does not need a constructor. It should have the following functions:

### Smart Contract FizzBuzz

Create a function called `fizzBuzz` that accepts a `uint` called `_number` and returns a `string memory`. The function should return:

- "Fizz" if the `_number` is divisible by 3
- "Buzz" if the `_number` is divisible by 5
- "FizzBuzz" if the `_number` is divisible by 3 and 5
- "Splat" if none of the above conditions are true

### Do Not Disturb

Create a function called `doNotDisturb` that accepts a `uint` called `_time`, and returns a `string memory`. It should adhere to the following properties:

- If `_time` is greater than or equal to 2400, trigger a `panic`
- If `_time` is greater than 2200 or less than 800, `revert` with a custom error of `AfterHours`, and include the time provided
- If `_time` is between `1200` and `1259`, `revert` with a string message "At lunch!"
- If `_time` is between 800 and 1199, return "Morning!"
- If `_time` is between 1300 and 1799, return "Afternoon!"
- If `_time` is between 1800 and 2200, return "Evening!"

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={2}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/learning-objectives.md -->

<!--
This file is automatically generated by a script. Do not edit it directly.
Use the script to regenerate this file.
-->

### [Ethereum Applications](./introduction-to-ethereum/ethereum-applications.md)

- Describe the origin and goals of the Ethereum blockchain
- List common types of applications that can be developed with the Ethereum blockchain
- Compare and contrast Web2 vs. Web3 development
- Compare and contrast the concept of "ownership" in Web2 vs. Web3

### [Gas Use in Ethereum Transactions](./introduction-to-ethereum/gas-use-in-eth-transactions.md)

- Explain what gas is in Ethereum
- Explain why gas is necessary in Ethereum
- Understand how gas works in Ethereum transactions

### [EVM Diagram](./introduction-to-ethereum/evm-diagram.md)

- Diagram the EVM

### [Setup and Overview](./hardhat-setup-overview/hardhat-setup-overview-sbs.md)

- Install and create a new Hardhat project with Typescript support
- Describe the organization and folder structure of a Hardhat project
- List the use and properties of hardhat.config.ts

### [Testing with Hardhat and Typechain](./hardhat-testing/hardhat-testing-sbs.md)

- Set up TypeChain to enable testing
- Write unit tests for smart contracts using Mocha, Chai, and the Hardhat Toolkit
- Set up multiple signers and call smart contract functions with different signers

### [Etherscan](./etherscan/etherscan-sbs.md)

- List some of the features of Etherscan
- Read data from the Bored Apes Yacht Club contract on Etherscan
- Write data to a contract using Etherscan.

### [Deploying Smart Contracts](./hardhat-deploy/hardhat-deploy-sbs.md)

- Deploy a smart contract to the Base Sepolia Testnet with hardhat-deploy
- Deploy a smart contract to the Sepolia Testnet with hardhat-deploy
- Use BaseScan to view a deployed smart contract

### [Verifying Smart Contracts](./hardhat-verify/hardhat-verify-sbs.md)

- Verify a deployed smart contract on Etherscan
- Connect a wallet to a contract in Etherscan
- Use etherscan to interact with your own deployed contract

### [Hardhat Forking](./hardhat-forking/hardhat-forking.md)

- Use Hardhat Network to create a local fork of mainnet and deploy a contract to it
- Utilize Hardhat forking features to configure the fork for several use cases

### ['Introduction to Remix'](./introduction-to-solidity/introduction-to-remix.md)

- List the features, pros, and cons of using Remix as an IDE
- Deploy and test the Storage.sol demo contract in Remix

### [Deployment in Remix](./introduction-to-solidity/deployment-in-remix.md)

- Deploy and test the Storage.sol demo contract in Remix

### [Hello World](./contracts-and-basic-functions/hello-world-step-by-step.md)

- Construct a simple "Hello World" contract
- List the major differences between data types in Solidity as compared to other languages
- Select the appropriate visibility for a function

### [Basic Types](./contracts-and-basic-functions/basic-types.md)

- Categorize basic data types
- List the major differences between data types in Solidity as compared to other languages
- Compare and contrast signed and unsigned integers

### [Test Networks](./deployment-to-testnet/test-networks.md)

- Describe the uses and properties of the Base testnet
- Compare and contrast Ropsten, Rinkeby, Goerli, and Sepolia

### [Deployment to Base Sepolia](./deployment-to-testnet/deployment-to-base-sepolia-sbs.md)

- Deploy a contract to the Base Sepolia testnet and interact with it in [BaseScan]

### [Contract Verification](./deployment-to-testnet/contract-verification-sbs.md)

- Verify a contract on the Base Sepolia testnet and interact with it in [BaseScan]

### [Control Structures](./control-structures/control-structures.md)

- Control code flow with `if`, `else`, `while`, and `for`
- List the unique constraints for control flow in Solidity
- Utilize `require` to write a function that can only be used when a variable is set to `true`
- Write a `revert` statement to abort execution of a function in a specific state
- Utilize `error` to control flow more efficiently than with `require`

### [Storing Data](./storage/simple-storage-sbs.md)

- Use the constructor to initialize a variable
- Access the data in a public variable with the automatically generated getter
- Order variable declarations to use storage efficiently

### [How Storage Works](./storage/how-storage-works.md)

- Diagram how a contract's data is stored on the blockchain (Contract -> Blockchain)
- Order variable declarations to use storage efficiently
- Diagram how variables in a contract are stored (Variable -> Contract)

### [Arrays](./arrays/arrays-in-solidity.md)

- Describe the difference between storage, memory, and calldata arrays

### [Filtering an Array](./arrays/filtering-an-array-sbs.md)

- Write a function that can return a filtered subset of an array

### [Mappings](./mappings/mappings-sbs.md)

- Construct a Map (dictionary) data type
- Recall that assignment of the Map data type is not as flexible as for other data types/in other languages
- Restrict function calls with the `msg.sender` global variable
- Recall that there is no collision protection in the EVM and why this is (probably) ok

### [Function Visibility and State Mutability](./advanced-functions/function-visibility.md)

- Categorize functions as public, private, internal, or external based on their usage
- Describe how pure and view functions are different than functions that modify storage

### [Function Modifiers](./advanced-functions/function-modifiers.md)

- Use modifiers to efficiently add functionality to multiple functions

### [Structs](./structs/structs-sbs.md)

- Construct a `struct` (user-defined type) that contains several different data types
- Declare members of the `struct` to maximize storage efficiency
- Describe constraints related to the assignment of `struct`s depending on the types they contain

### [Inheritance](./inheritance/inheritance-sbs.md)

- Write a smart contract that inherits from another contract
- Describe the impact inheritance has on the byte code size limit

### [Multiple Inheritance](./inheritance/multiple-inheritance.md)

- Write a smart contract that inherits from multiple contracts

### [Abstract Contracts](./inheritance/abstract-contracts-sbs.md)

- Use the virtual, override, and abstract keywords to create and use an abstract contract

### [Imports](./imports/imports-sbs.md)

- Import and use code from another file
- Utilize OpenZeppelin contracts within Remix

### [Error Triage](./error-triage/error-triage.md)

- Debug common solidity errors including transaction reverted, out of gas, stack overflow, value overflow/underflow, index out of range, etc.

### [The New Keyword](./new-keyword/new-keyword-sbs.md)

- Write a contract that creates a new contract with the new keyword

### ['Contract to Contract Interaction'](./interfaces/contract-to-contract-interaction.md)

- Use interfaces to allow a smart contract to call functions in another smart contract
- Use the `call()` function to interact with another contract without using an interface

### [Events](./events/hardhat-events-sbs.md)

- Write and trigger an event
- List common uses of events
- Understand events vs. smart contract storage

### [Address and Payable in Solidity](./address-and-payable/address-and-payable.md)

- Differentiate between address and address payable types in Solidity
- Determine when to use each type appropriately in contract development
- Employ address payable to send Ether and interact with payable functions

### [Minimal Token](./minimal-tokens/minimal-token-sbs.md)

- Construct a minimal token and deploy to testnet
- Identify the properties that make a token a token

### [The ERC-20 Token Standard](./erc-20-token/erc-20-standard.md)

- Analyze the anatomy of an ERC-20 token
- Review the formal specification for ERC-20

### [ERC-20 Implementation](./erc-20-token/erc-20-token-sbs.md)

- Describe OpenZeppelin
- Import the OpenZeppelin ERC-20 implementation
- Describe the difference between the ERC-20 standard and OpenZeppelin's ERC20.sol
- Build and deploy an ERC-20 compliant token

### [The ERC-721 Token Standard](./erc-721-token/erc-721-standard.md)

- Analyze the anatomy of an ERC-721 token
- Compare and contrast the technical specifications of ERC-20 and ERC-721
- Review the formal specification for ERC-721

### [ERC-721 Token](./erc-721-token/erc-721-sbs.md)

- Analyze the anatomy of an ERC-721 token
- Compare and contrast the technical specifications of ERC-20 and ERC-721
- Review the formal specification for ERC-721
- Build and deploy an ERC-721 compliant token
- Use an ERC-721 token to control ownership of another data structure

### [Wallet Connectors](./frontend-setup/wallet-connectors.md)

- Identify the role of a wallet aggregator in an onchain app
- Debate the pros and cons of using a template
- Scaffold a new onchain app with RainbowKit
- Support users of EOAs and the Coinbase Smart Wallet with the same app

### [Building an Onchain App](./frontend-setup/building-an-onchain-app.md)

- Identify the role of a wallet aggregator in an onchain app
- Debate the pros and cons of using a template
- Add a wallet connection to a standard template app

### [The `useAccount` Hook](./reading-and-displaying-data/useAccount.md)

- Implement the `useAccount` hook to show the user's address, connection state, network, and balance
- Implement an `isMounted` hook to prevent hydration errors

### [The `useReadContract` Hook](./reading-and-displaying-data/useReadContract.md)

- Implement wagmi's `useReadContract` hook to fetch data from a smart contract
- Convert data fetched from a smart contract to information displayed to the user
- Identify the caveats of reading data from automatically-generated getters

### [Configuring `useReadContract`](./reading-and-displaying-data/configuring-useReadContract.md)

- Use `useBlockNumber` and the `queryClient` to automatically fetch updates from the blockchain
- Describe the costs of using the above, and methods to reduce those costs
- Configure arguments to be passed with a call to a `pure` or `view` smart contract function
- Call an instance of `useReadContract` on demand
- Utilize `isLoading` and `isFetching` to improve user experience

### [The `useWriteContract` hook](./writing-to-contracts/useWriteContract.md)

- Implement wagmi's `useWriteContract` hook to send transactions to a smart contract
- Configure the options in `useWriteContract`
- Display the execution, success, or failure of a function with button state changes, and data display

### [The `useSimulateContract` hook](./writing-to-contracts/useSimulateContract.md)

- Implement wagmi's `useSimulateContract` and `useWriteContract` to send transactions to a smart contract
- Configure the options in `useSimulateContract` and `useWriteContract`
- Call a smart contract function on-demand using the write function from `useWriteContract`, with arguments and a value



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/erc-721-exercise.md -->

---
title: ERC-721 Tokens Exercise
description: Exercise - Create your own NFT!
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a contract called `HaikuNFT`. Add the following to the contract:

- A `struct` called `Haiku` to store the `address` of the `author` and `line1`, `line2`, and `line3`
- A public array to store these `haikus`
- A public `mapping` to relate `sharedHaikus` from the `address` of the wallet shared with, to the id of the Haiku NFT shared
- A public `counter` to use as the id and to track and share the total number of Haikus minted
  - If 10 Haikus have been minted, the counter should be at 11, to serve as the next id
  - Do **NOT** assign an id of 0 to a haiku
- Other variables as necessary to complete the task

Add the following functions.

### Constructor

As appropriate.

### Mint Haiku

Add an `external` function called `mintHaiku` that takes in the three lines of the poem. This function should mint an NFT for the minter and save their Haiku.

Haikus must be **unique**! If any line in the Haiku has been used as any line of a previous Haiku, revert with `HaikuNotUnique()`.

You **don't** have to count syllables, but it would be neat if you did! (No promises on whether or not we counted the same as you did)

### Share Haiku

Add a `public` function called `shareHaiku` that allows the owner of a Haiku NFT to share that Haiku with the designated `address` they are sending it `_to`. Doing so should add it to that address's entry in `sharedHaikus`.

If the sender isn't the owner of the Haiku, instead revert with an error of `NotYourHaiku`. Include the id of the Haiku in the error.

:::danger

Remember, everything on the blockchain is public. This sharing functionality can be expanded for features similar to allowing an app user to display the selected shared haiku on their profile.

It does nothing to prevent anyone and everyone from seeing or copy/pasting the haiku!

:::

### Get Your Shared Haikus

Add a `public` function called `getMySharedHaikus`. When called, it should return an array containing all of the haikus shared with the caller.

If there are no haikus shared with the caller's wallet, it should revert with a custom error of `NoHaikusShared`, with no arguments.

---

:::caution

The contract specification contains actions that can only be performed once by a given address. As a result, the unit tests for a passing contract will only be successful the **first** time you test.

**You may need to submit a fresh deployment to pass**

:::

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={15}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/erc-721-on-opensea-vid.md -->

---
title: ERC-721 Token On Opensea
description: Learn how a popular marketplace interprets tokens.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='813634970' title='ERC-721 On OpenSea' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/openzeppelin-erc-721-vid.md -->

---
title: OpenZeppelin ERC-721 Implementation
description: Review  the ERC-721 implementation by OpenZeppelin.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='813635078' title='OpenZeppelin ERC-721 Implementation' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/implementing-an-erc-721-vid.md -->

---
title: Implementing an ERC-721
description: Deploy your own NFT.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='813635046' title='Implementing an ERC-721 Token' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/erc-721-standard-video.md -->

---
title: ERC-721 Token Standard
description: Review the formal standard for the ERC-721 Token.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='813634992' title='ERC-721 Standard Overview' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/erc-721-sbs.md -->

---
title: ERC-721 Token
description: Build your own NFT based on the ERC-721 standard.
hide_table_of_contents: false
---

Punks, Apes, and birds of all kinds. You've heard about them, seen them, and may even be lucky enough to own a famous NFT. Or maybe you've just bought into a random collection and aren't sure what to do with your NFT. NFTs aren't really pictures, or anything else specific. They're a method of proving ownership of a digital asset. Anyone can right-click on a picture of a monkey and set it as their profile picture, but only the owner can use it with apps that utilize web3 ownership.

The ERC-721 token standard is the underlying technical specification that not only makes digital ownership possible, it provides a standardized way for marketplaces, galleries, and other sites to know how to interact with these digital items.

---

## Objectives

By the end of this lesson you should be able to:

- Analyze the anatomy of an ERC-721 token
- Compare and contrast the technical specifications of ERC-20 and ERC-721
- Review the formal specification for ERC-721
- Build and deploy an ERC-721 compliant token
- Use an ERC-721 token to control ownership of another data structure

---

## Implementing the OpenZeppelin ERC-721 Token

JPGs may be all the rage right now but in the future, the selfie you post on social media, a text message you send to your mother, and the +4 battleaxe you wield in your favorite MMO might all be NFTs.

### Import and Setup

Start by opening the [OpenZeppelin] ERC-721 in Github. Copy the link and use it to import the ERC-721 contract. Create your own contract, called `MyERC721`, that inherits from `ERC721Token`. Add a constructor that initializes the `_name` and `_symbol`.

<details>

<summary>Reveal code</summary>

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";

contract MyERC721Token is ERC721 {
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {

    }
}
```

</details>

<br/>

### Minting NFTs

The minting function that is provided by OpenZeppelin, `_safeMint`, is `internal`. To use it to let your customers mint NFTs, you'll need to implement a function in your contract that calls the one in the imported contract.

Before you can do that, you need a way to supply the two parameters needed for `_safeMint`:

- `address to` - the owner of the new NFT
- `uint256 tokenId` - the ID number for the new NFT

The owner is easy, you can simply use `msg.sender` to grant ownership to the wallet doing the minting.

ID is slightly more challenging. A common practice is to simply assign the total number of NFTs, including the one being minted, as the `tokenId`. Doing so is straightforward, makes it easier to find all of the NFTs within a collection, and helps lean in to the common community perception that lower-number NFTs are better, just like other limited-edition collectibles.

:::caution
Obfuscating certain information, such as customer IDs, is often considered a best practice. Doing so might make it harder for an attacker who has circumvented other security functions from getting access to more data. If `134` is a valid `customer_id`, it is likely that `135` is too. The same can't be said for `bfcb51bd-c04f-42d5-8116-3def754e8c32`.

This practice is not as useful on the blockchain, because all information is public.
:::

To implement ID generation, simply add a `uint` called `counter` to storage and initialize it as 1, either at declaration or in the constructor.

Now, you can add a function called `redeemNFT` that calls `safeMint` using the `msg.sender` and `counter`, and then increments the `counter`:

<details>

<summary>Reveal code</summary>

```solidity
function redeemNFT() external {
    _safeMint(msg.sender, counter);
    counter++;
}
```

</details>

<br/>

:::danger

As a programmer, you've probably gone through great pains to internalize the idea of zero-indexing. Arrays start at 0. The pixel in the top-left corner of your screen is located at 0, 0.

As a result, you need to be very careful when working with Solidity because there isn't the concept of `undefined`, and "deleted" values return to their default value, which is 0 for numbers.

To prevent security risks, you'll need to make sure that you never give an ID or array index of 0 to anything. Otherwise, attempting to delete a value, such as a `struct` member called `authorizedSellerID` might give the wallet address stored at index 0 access to that resource.

:::

Deploy and test. Be sure to:

- Mint several NFTs
- Transfer an NFT from one Remix account to another
- Try to transfer an NFT to `0x0000000000000000000000000000000000000000`

---

## ERC-721 URIs

The ERC-721 standard includes the option to define a [URI] associated with each NFT. These are intended to point to a `json` file following the _ERC721 Metadata JSON Schema_

```json
{
  "title": "Asset Metadata",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Identifies the asset to which this NFT represents"
    },
    "description": {
      "type": "string",
      "description": "Describes the asset to which this NFT represents"
    },
    "image": {
      "type": "string",
      "description": "A URI pointing to a resource with mime type image/* representing the asset to which this NFT represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
    }
  }
}
```

Note that they don't have to. In the OpenZeppelin implementation, the function that returns the `_baseURI` is `virtual` and must be overridden by an inheriting contract.

```
// OpenZeppelin ERC-721
/**
    * @dev Base URI for computing {tokenURI}. If set, the resulting URI for each
    * token will be the concatenation of the `baseURI` and the `tokenId`. Empty
    * by default, can be overridden in child contracts.
    */
function _baseURI() internal view virtual returns (string memory) {
    return "";
}
```

The owner of the contract can therefore choose what the value is and when, how, or if it is changeable. For example, the [Bored Ape Yacht Club] contract has a function allowing the owner to set or change the \_baseURI, changing where the metadata is stored, and potentially what is in it.

```solidity
// From boredapeyachtclub.sol
function setBaseURI(string memory baseURI) public onlyOwner {
    _setBaseURI(baseURI);
}
```

The metadata for [BAYC] is [stored on IPFS], but some projects even use centralized, web2 storage options!

### NFT Switcheroo

[Doodles] is another NFT collection that [uses IPFS] to store metadata. Let's modify our contract to swap metadata back and forth from one collection to the other.

Start by saving the IPFS metadata bases as constants, at the contract level. Add an enum to enable selection between these two choices, and an instance of that enum.

<details>

<summary>Reveal code</summary>

```solidity
    string constant BAYC = "https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/";
    string constant DOODLES = "https://ipfs.io/ipfs/QmPMc4tcBsMqLRuCQtPmPe84bpSjrC3Ky7t3JWuHXYB4aS/";

    enum NFTMetadata { BAYC, DOODLES }
    NFTMetadata nftMetadata = NFTMetadata.BAYC;
```

</details>

<br/>

Finally, add an override of `_baseURI` that returns the appropriate selection based on which collection is active, and a function to swap the URI.

<details>

<summary>Reveal code</summary>

```solidity
function _baseURI() internal override view returns(string memory) {
    if (nftMetadata == NFTMetadata.BAYC) {
        return BAYC;
    } else if (nftMetadata == NFTMetadata.DOODLES){
        return DOODLES;
    } else {
        revert("Error...");
    }
}

function switchURI() public {
    // TODO: Limit to contract owner
    nftMetadata = nftMetadata == NFTMetadata.BAYC ? NFTMetadata.DOODLES : NFTMetadata.BAYC;
}
```

</details>

<br/>

Deploy, mint some NFTs, and call `tokenURI` to find the information for token number 1. You should get:

```text
https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/1
```

This links to the metadata json file for the first Bored Ape:

```json
{
  "image": "ipfs://QmPbxeGcXhYQQNgsC6a36dDyYUcHgMLnGKnF8pVFmGsvqi",
  "attributes": [
    {
      "trait_type": "Mouth",
      "value": "Grin"
    },
    {
      "trait_type": "Clothes",
      "value": "Vietnam Jacket"
    },
    {
      "trait_type": "Background",
      "value": "Orange"
    },
    {
      "trait_type": "Eyes",
      "value": "Blue Beams"
    },
    {
      "trait_type": "Fur",
      "value": "Robot"
    }
  ]
}
```

IPFS links don't work natively directly in the browser, but you can see the image here:

https://ipfs.io/ipfs/QmPbxeGcXhYQQNgsC6a36dDyYUcHgMLnGKnF8pVFmGsvqi/

Now, call your `switchURI` function and then call `tokenURI` again for token 1.

Now, you'll get a new link for metadata:

```text
https://ipfs.io/ipfs/QmPMc4tcBsMqLRuCQtPmPe84bpSjrC3Ky7t3JWuHXYB4aS/1
```

Which contains the metadata for Doodle 1 instead of BAYC 1:

```json
{
  "image": "ipfs://QmTDxnzcvj2p3xBrKcGv1wxoyhAn2yzCQnZZ9LmFjReuH9",
  "name": "Doodle #1",
  "description": "A community-driven collectibles project featuring art by Burnt Toast. Doodles come in a joyful range of colors, traits and sizes with a collection size of 10,000. Each Doodle allows its owner to vote for experiences and activations paid for by the Doodles Community Treasury. Burnt Toast is the working alias for Scott Martin, a Canadian\u2013based illustrator, designer, animator and muralist.",
  "attributes": [
    {
      "trait_type": "face",
      "value": "holographic beard"
    },
    {
      "trait_type": "hair",
      "value": "white bucket cap"
    },
    {
      "trait_type": "body",
      "value": "purple sweater with satchel"
    },
    {
      "trait_type": "background",
      "value": "grey"
    },
    {
      "trait_type": "head",
      "value": "gradient 2"
    }
  ]
}
```

Your robot ape is now a person with a rainbow beard!

https://ipfs.io/ipfs/QmTDxnzcvj2p3xBrKcGv1wxoyhAn2yzCQnZZ9LmFjReuH9

---

## Conclusion

In this lesson, you've learned how to use OpenZeppelin's ERC-721 implementation to create your own NFT contract. You've also learned how NFT metadata is stored, and that it is not necessarily immutable.

---

[OpenZeppelin]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol
[Coinbase NFT]: https://nft.coinbase.com/
[URI]: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
[stored on IPFS]: https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/
[BAYC]: https://nft.coinbase.com/collection/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d
[CryptoPunks]: https://nft.coinbase.com/collection/ethereum/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb
[Doodles]: https://nft.coinbase.com/collection/ethereum/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e
[uses IPFS]: https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-721-token/erc-721-standard.md -->

---
title: The ERC-721 Token Standard
description: An overview of the ERC-721 token standard
hide_table_of_contents: false
---

In this article, we'll delve into the ERC-721 token standard, exploring its technical specs, applications, and how it differs from the ERC-20 standard.

---

## Objectives:

By the end of this lesson you should be able to:

- Analyze the anatomy of an ERC-721 token
- Compare and contrast the technical specifications of ERC-20 and ERC-721
- Review the formal specification for ERC-721

---

## Introduction

The development of the Ethereum ecosystem has been marked by key milestones, two of which are the inception of the ERC-20 and ERC-721 token standards. While ERC-20 provided a foundational framework for fungible tokens, ERC-721 established a flexible and adaptable infrastructure for non-fungible tokens (NFTs).

The ERC-721 token standard is pivotal in the Ethereum ecosystem for creating and managing unique digital assets. With its consistent rules and functions, it has greatly enhanced the user experience, solidifying its position as the go-to standard for non-fungible tokens. ERC-721 has been instrumental in expanding the digital collectibles market and spurring the development of new applications and services.

![The Evolution of the Ethereum Ecosystem](../../assets/images/erc-721/evolution-eth-erc721.png)

---

## ERC-721 Specification

EIP-721 (Ethereum Improvement Proposal 721) is the formal specification for ERC-721, defining the requirements for creating compliant non-fungible tokens on Ethereum. EIP-721 prescribes mandatory functions and events that a token must implement to achieve ERC-721 compliance. Adherence to EIP-721 ensures compatibility of unique tokens with existing Ethereum applications and services, simplifying integration.

---

## Anatomy of an ERC-721 Token

An ERC-721 token comprises a smart contract implementing the standardized interface, which includes six primary functions:

- **balanceOf(address)** Returns the number of tokens held by a specific address.
- **ownerOf(uint256):** Provides the owner of a specified token.
- **safeTransferFrom(address, address, uint256):** Transfers a specific token's ownership from one address to another.
- **transferFrom(address, address, uint256):** Allows a third party to transfer tokens on the token owner's behalf, given the owner's approval.
- **approve(address, uint256):** Enables the token owner to permit a third party to transfer a specific token on their behalf.
- **getApproved(uint256):** Shows the approved address for a specific token.

These functions ensure each ERC-721 token has a unique identifier and can be owned and transferred individually.

---

## ERC-721 Vs ERC-20

The ERC-721 and ERC-20 token standards share a common goal of providing a set of standards for tokens on the Ethereum network but diverge in terms of functionality and use cases.

ERC-20 tokens are fungible, meaning each token is identical to every other token; they are interchangeable like currency. On the other hand, ERC-721 tokens are non-fungible, meaning each token is unique and not interchangeable with any other token. This uniqueness is made possible through the ownerOf() and getApproved() functions, which provide information about the ownership of each unique token.

The ERC-20 standard has primarily found use in creating cryptocurrencies for apps, governance tokens, utility tokens, stablecoins, and more. The ERC-721 standard, conversely, has been adopted largely for creating unique digital assets like collectibles, digital art, and tokenized virtual real estate, among other applications.

---

## Benefits of ERC-721 Standardization

Standardizing non-fungible tokens via the ERC-721 token standard presents substantial benefits to developers and users in the Ethereum ecosystem. Developers have access to a standardized set of functions, leading to less code ambiguity, fewer errors, and a streamlined development process. This uniformity also ensures smooth integration with existing apps and platforms on Ethereum.

For users, the ERC-721 standard offers an intuitive, consistent interface for interacting with a wide array of unique tokens. Regardless of the token's specific use or design, users can reliably check their ownership of tokens, transfer tokens to other addresses, and approve transactions. This consistency enhances usability across the Ethereum platform, from digital art marketplaces to tokenized real estate and gaming applications.

![The Benefits of ERC-721 Standardization](../../assets/images/erc-721/erc-721-standard.png)

---

## Applications

ERC-721 tokens find wide-ranging applications in various categories:

- **Digital Art:** Artists can create unique digital artworks as ERC-721 tokens. These tokens can be sold or traded on platforms like OpenSea, Rarible, and Coinbase NFT. Examples include work by the digital artist Beeple.

- **Gaming:** Game assets such as characters, items, and land can be tokenized as ERC-721 tokens, providing players with true ownership of their in-game assets. Examples include Axie Infinity and Decentraland.

- **Collectibles:** ERC-721 tokens can represent unique collectible items in a digital space. Examples include NBA Top Shot moments and CryptoPunks.

- **Virtual Real Estate:** Virtual real estate can be tokenized as ERC-721 tokens, providing proof of ownership and facilitating trade on virtual platforms. Examples include parcels of land in Cryptovoxels and Decentraland.

---

## Conclusion

ERC-721, with its consistent framework for non-fungible tokens, has revolutionized the unique digital asset space on Ethereum. This standard, when contrasted with ERC-20, highlights Ethereum's capacity for both fungible and unique asset types. Adhering to the EIP-721 specification, ERC-721 tokens have significantly influenced the Ethereum-based digital economy. From digital art to gaming, these tokens underscore their importance and role as catalysts in the burgeoning NFT revolution.

---

## See Also

- [EIP-721: ERC-721 Token Standard](https://eips.ethereum.org/EIPS/eip-721)
- [ERC-721 Token Standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/)



<!-- File: ../web/apps/base-docs/base-learn/docs/frontend-setup/overview.md -->

---
title: 'Overview'
description: An overview of this course.
hide_table_of_contents: false
---

Welcome! The course you are about to begin will rapidly introduce you to frontend web development for onchain apps and enable you to write websites that can call your smart contract functions in a similar way to how traditional sites interact with APIs.

## Prerequisites

Before these lessons, you should:

- Be comfortable with traditional frontend development using React, ideally with NextJS
- Possess a general understanding of the EVM and smart contracts

---

## Objectives

By the end of this course, you should be able to:

- **Frontend Setup**
  - Identify the role of a wallet aggregator in an onchain app
  - Debate the pros and cons of using a template
  - Scaffold a new onchain app with RainbowKit
  - Add a wallet connection to a standard template app
- **Connecting to the Blockchain**
  - Compare and contrast public providers vs. vendor providers vs. wallet providers
  - Select the appropriate provider for several use cases
  - Set up a provider in wagmi and use it to connect a wallet
  - Protect API keys that will be exposed to the front end
- **Reading and Displaying Data**
  - Implement the `useAccount` hook to show the user's address, connection state, network, and balance
  - Implement an `isMounted` hook to prevent hydration errors
  - Implement wagmi's `useReadContract` hook to fetch data from a smart contract
  - Convert data fetched from a smart contract to information displayed to the user
  - Identify the caveats of reading data from automatically-generated getters
  - Enable the `watch` feature of `useReadContract` to automatically fetch updates from the blockchain
  - Describe the costs of using the `watch` feature, and methods to reduce those costs
  - Configure arguments to be passed with a call to a `pure` or `view` smart contract function
  - Call an instance of `useReadContract` on demand
  - Utilize `isLoading` and `isFetching` to improve user experience
- **Writing to Contracts**
  - Implement wagmi's `useWriteContract` hook to send transactions to a smart contract
  - Configure the options in `useWriteContract`
  - Display the execution, success, or failure of a function with button state changes, and data display
  - Implement Wagmi's `usePrepareContractWrite` and `useWriteContract` to send transactions to a smart contract
  - Configure the options in `useSimulateContract` and `useWriteContract`
  - Call a smart contract function on-demand using the write function from `useWriteContract`, with arguments and a value

---



<!-- File: ../web/apps/base-docs/base-learn/docs/frontend-setup/wallet-connectors.md -->

---
title: Wallet Connectors
description: Learn about how wallet connector libraries aggregate wallets and make it easier to connect to them from your app.
hide_table_of_contents: false
---

One of the most intimidating tasks when building an onchain app is making that initial connection between your users' wallets, and your app. Initial research often surfaces a bewildering number of wallets, each with their own SDKs, and own methods to manage the connection. Luckily, you don't actually need to manage all of this on your own. There are a number of wallet connector libraries specialized in creating a smooth and beautiful user experience to facilitate this connection.

To further add to the confusion and difficulty, [Smart wallets] are growing in popularity. These advanced wallets allow users to create and manage wallets with [passkeys], and support, or will soon support, a growing array of features including session keys, account recovery, and more!

[RainbowKit], the aggregator you'll use for this lesson, works with the Coinbase Smart Wallet out of the box, but you'll need to do a little bit of extra configuration to support users of both traditional wallets and smart wallets.

---

## Objectives

By the end of this guide you should be able to:

- Identify the role of a wallet aggregator in an onchain app
- Debate the pros and cons of using a template
- Scaffold a new onchain app with RainbowKit
- Support users of EOAs and the Coinbase Smart Wallet with the same app

---

## Connecting to the Blockchain

One of the many challenging tasks of building a frontend that can interface with your smart contracts is managing the user's connection between your onchain app and their [EOA] wallet. Not only is there an ever-growing suite of different wallets, but users can (and probably should!) use several different addresses within the same wallet app.

[Rainbowkit] is one of several options that makes this a little bit easier by serving as an aggregator of wallets, and handling some of the details of connecting them. Alternatives include [ConnectKit], and [Dynamic], which are both excellent choices as well.

Each of these include customizable UI/UX components for inviting the user to connect, displaying connection status, and selecting which wallet they wish to use.

### Using the Quick Start

If you're just trying to get up and running as quickly as possible, you can use RainbowKit's [quick start] script to scaffold an app from their template, with a single command. If you're using Yarn:

```bash
yarn create @rainbow-me/rainbowkit
```

:::info

The script doesn't accept `.` as a project name, so you'll want to run this script in your `src` directory, or wherever you keep your projects. It will create a folder with the same name as your project, and install the project files inside.

:::

Once it's done, simply run the app with:

```bash
yarn run dev
```

Using the script is fast, but it does mean less choice. In this case, it builds the app on top of [Next.js], which is great if you want to use it, but not helpful if you prefer to work from a different framework, such as [Create React App], or [Remix] (the React framework, not the Solidity IDE). The script also doesn't help you if you want to add an onchain integration to an existing site.

:::info

The Rainbowkit template has been updated to wagmi 2.X, but it does **not** use the Next.js app router. You'll need to install it manually if you wish to use the latest patterns.

The [Building an Onchain App] tutorial will show you how to do this!

:::

### Coinbase Smart Wallet

If you have the Coinbase Wallet extension, you might be wondering where the smart wallet can be found. By default, the smart wallet will only be invoked if you click the `Coinbase Wallet` button to log in **and** you **don't** have the browser extension. To test, open a private window with extensions disabled and try to log in.

Selecting `Rainbow`, `MetaMask`, or `WalletConnect` will display a QR code so that the user can log in with their phone. Picking `Coinbase Wallet` will instead invoke the smart wallet login.

This flow can be improved upon, as new crypto users won't know that digging for the smart wallet is the best path forward, and existing users who are trying to migrate to the smart wallet don't have that option.

See our tutorial on how to [Use the Coinbase Smart Wallet and EOAs with OnchainKit] for more details!

---

## Conclusion

In this article, you've learned how libraries such as [Rainbowkit], [ConnectKit], and [Dynamic], aggregate wallets and make it easier for you to connect your app to your users' wallet of choice. You've also learned how you can use a template to quickly create the foundation of your app. Finally, you've learned that the cost of using a template is that it does make some choices for you.

---

[RainbowKit]: https://www.rainbowkit.com/
[wagmi]: https://wagmi.sh/
[wallet]: https://ethereum.org/en/developers/docs/accounts/
[ConnectKit]: https://ethereum.org/en/developers/docs/accounts/
[Dynamic]: https://www.dynamic.xyz/
[quick start]: https://www.rainbowkit.com/docs/installation
[Next.js]: https://nextjs.org/
[Create React App]: https://create-react-app.dev/
[Remix]: https://remix.run/
[Building an Onchain App]: ./building-an-onchain-app
[Smart wallets]: https://www.coinbase.com/wallet/smart-wallet
[passkeys]: https://safety.google/authentication/passkey/
[Use the Coinbase Smart Wallet and EOAs with OnchainKit]: https://docs.base.org/tutorials/smart-wallet-and-eoa-with-onchainkit



<!-- File: ../web/apps/base-docs/base-learn/docs/frontend-setup/building-an-onchain-app.md -->

---
title: Building an Onchain App
description: Learn step-by-step how to turn a regular template app into an onchain app with a wallet connection.
hide_table_of_contents: false
---

While it's convenient and fast to start from a template, the template may not fit your needs. Whether you prefer a different stack, or have already started building the traditional web components of your app, it's common to need to manually add onchain libraries to get your app working.

In this guide, you'll build the beginnings of an app similar to the one created by the [RainbowKit] quick start, but you'll do it piece by piece. You can follow along, and swap out any of our library choices with the ones you prefer.

---

## Objectives

By the end of this guide you should be able to:

- Identify the role of a wallet aggregator in an onchain app
- Debate the pros and cons of using a template
- Add a wallet connection to a standard template app

---

## Creating the Traditional App

Start by running the [Next.js] script to create a Next.js app:

```bash
npx create-next-app@latest --use-yarn
```

This script will accept `.`, if you want to add the project to the root of a folder you've already created. Otherwise, name your project. Select each option in the generation script as you see fit. We recommend the following selections:

- Use Typescript?: Yes
- Use ESLint?: Yes
- Use Tailwind?: Your preference
- Use `src/` directory?: Yes
- Use App Router?: Yes
- Customize the default import alias?: No

:::info

The default Next.js script installs [Tailwind]. [RainbowKit]'s does not.

:::

Run your app with `yarn dev` to make sure it generated correctly.

### Manually Installing RainbowKit, Wagmi, and Viem

The [quick start] guide for RainbowKit also contains step-by-step instructions for manual install. You'll be following an adjusted version here. Most of the setup is actually for configuring [wagmi], which sits on top of [viem] and makes it much easier to write React that interacts with the blockchain.

Start by installing the dependencies:

```bash
npm install @rainbow-me/rainbowkit wagmi viem@2.x @tanstack/react-query
```

:::info
Onchain libraries and packages tend to require very current versions of Node. If you're not already using it, you may want to install [nvm].
:::

## Adding Imports, Connectors, Config

In Next.js with the app router, the root of your app is found in `app/layout.tsx`, if you followed the recommended setup options. As you want the blockchain provider context to be available for the entire app, you'll add it here.

You'll need to set up your providers in a second file, so that you can add `'use client';` to the top. Doing so forces this code to be run client side, which is necessary since your server won't have access to your users' wallet information.

:::caution

You must configure these wrappers in a separate file. It will not work if you try to add them and `'use client';` directly in `layout.tsx`!

:::

Add a new file in the `app` folder called `providers.tsx`.

### Imports

As discussed above, add `'use client';` to the top of the file.

Continue with the imports:

```tsx
import '@rainbow-me/rainbowkit/styles.css';
import { useState, type ReactNode } from 'react';
import { getDefaultConfig, RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { WagmiProvider } from 'wagmi';
import { base, baseSepolia } from 'wagmi/chains';
import { QueryClientProvider, QueryClient } from '@tanstack/react-query';
```

:::caution

If you're adapting this guide to a different set of libraries or platforms, you may need to import `styles.css` differently. You'll know this is the case if you get ugly text at the bottom of the page instead of a nice modal when you click the connect button.

:::

### Config

Now, you need to configure the chains, wallet connectors, and providers for your app. You'll use `getDefaultConfig` for now, to get started. See our guide on [Connecting to the Blockchain] for more information on blockchain providers.

:::info

To take advantage of a more advanced set of options with [OnchainKit], see our tutorial on how to [Use the Coinbase Smart Wallet and EOAs with OnchainKit]. If you just want to customize the list of wallets in [RainbowKit], see our tutorial for [Coinbase Smart Wallet with RainbowKit].

:::

You'll need a `projectId` from [Wallet Connect Cloud], which you can get for free on their site. Make sure to insert it in the appropriate place.

:::danger

Remember, everything on the frontend is public! Be sure to configure the allowlist for your WalletConnect id!

:::

```tsx
const config = getDefaultConfig({
  appName: 'Cool Onchain App',
  projectId: 'YOUR_PROJECT_ID',
  chains: [base, baseSepolia],
  ssr: true, // If your dApp uses server side rendering (SSR)
});
```

### Returning the Context Providers

[TanStack Query] is now a required dependency for wagmi, and you need to add it as a React context provider. The short version is that it helps with state management. Read the docs for the long version!

Add an exported function for the providers. This sets up the `QueryClient` and returns `props.children` wrapped in all of your providers.

```tsx
export function Providers(props: { children: ReactNode }) {
  const [queryClient] = useState(() => new QueryClient());

  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <RainbowKitProvider>{props.children}</RainbowKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

## Using Your new Providers

Open `layout.tsx`. Import your `Providers`, being careful if you use auto-import as there are many other things with similar names in the list. Wrap the `children` in your `return` with the new `Providers`.

```tsx
return (
  <html lang="en">
    <body className={inter.className}>
      <Providers>{children}</Providers>
    </body>
  </html>
);
```

## Adding the Connect Button

You're now ready to add your connect button. You can do this anywhere in your app, thanks to the `RainbowKitProvider`. Common practice would be to place the button in your app's header. Since the Next.js template doesn't have one, you can just add it to the top of the automatically generated page, rather than spending time implementing React components.

Open up `page.tsx`, and import the `ConnectButton`:

```tsx
import { ConnectButton } from '@rainbow-me/rainbowkit';
```

Then, simply add the `ConnectButton` component at the top of the first `<div>`:

```tsx
// This function has been simplified to save space.
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <ConnectButton />

        {/* Other Code...*/}
        </p>
      </div>
    </main>
  );
}
```

Run your app with `yarn dev`, and you should be able to use the RainbowKit connect button to connect with your wallet and switch between networks.

You use the [Connect Button] props to modify its properties, or you can [customize the connect button] extensively. Some users dislike having the connect button display their token balance. Try disabling it with:

```tsx
<ConnectButton showBalance={false} />
```

---

## Conclusion

In this guide, you've learned how to assemble your onchain app from several pieces. You can use this knowledge to integrate a wallet connection with an existing site, or adjust the stack to meet your preferences. Finally, you've learned how to insert and customize the connect button.

If you're looking to quickly bootstrap a simple app, you can always use a script, such as the RainbowKit [quick start]. If you're looking for a robust start for a consumer application, check out [OnchainKit]!

---

[RainbowKit]: https://www.rainbowkit.com/
[wagmi]: https://wagmi.sh/
[viem]: https://viem.sh/
[quick start]: https://www.rainbowkit.com/docs/installation
[Next.js]: https://nextjs.org/
[Tailwind]: https://tailwindcss.com/
[nvm]: https://github.com/nvm-sh/nvm
[WalletConnect]: https://cloud.walletconnect.com/
[Connecting to the Blockchain]: https://docs.base.org/connecting-to-the-blockchain/overview
[Wallet Connect Cloud]: https://cloud.walletconnect.com/
[Connect Button]: https://www.rainbowkit.com/docs/connect-button
[customize the connect button]: https://www.rainbowkit.com/docs/custom-connect-button
[TanStack Query]: https://tanstack.com/query/latest
[Coinbase Smart Wallet with RainbowKit]: https://docs.base.org/tutorials/smart-wallet-and-rainbowkit
[OnchainKit]: https://onchainkit.xyz/?utm_source=basedocs&utm_medium=tutorials&campaign=building-an-onchain-app
[Use the Coinbase Smart Wallet and EOAs with OnchainKit]: https://docs.base.org/tutorials/smart-wallet-and-eoa-with-onchainkit



<!-- File: ../web/apps/base-docs/base-learn/docs/exercise-contracts.md -->

---
title: 'Exercise Contracts'
description: A list of verified unit test contracts for Base Learn exercises.
keywords: [Solidity, Base Learn, NFT]
hide_table_of_contents: false
---

Many of the sections in Base Learn contain an exercise to test your knowledge on the material you have just completed. We tell you **what** to do, but not **how** to do it. You have to apply your knowledge and demonstrate the new abilities you have earned.

Upon success, you'll be granted a non-transferable, or soulbound, NFT as a memento of your learning. You can track your progress on the [progress page].

Below is a list of the exercises, with links to view their code. The unit tests are written in a bespoke framework in Solidity, but the patterns should be recognizable to most engineers.

| Exercise                 | Code                                         |
| :----------------------- | :------------------------------------------- |
| [Deploying to a Testnet] | [0x075eB9Dc52177Aa3492E1D26f0fDE3d729625d2F] |
| [Control Structures]     | [0xF4D953A3976F392aA5509612DEfF395983f22a84] |
| [Storage]                | [0x567452C6638c0D2D9778C20a3D59749FDCaa7aB3] |
| [Arrays]                 | [0x5B0F80cA6f5bD60Cc3b64F0377f336B2B2A56CdF] |
| [Mappings]               | [0xD32E3ACe3272e2037003Ca54CA7E5676f9b8D06C] |
| [Structs]                | [0x9eB1Fa4cD9bd29ca2C8e72217a642811c1F6176d] |
| [Inheritance]            | [0xF90dA05e77a33Fe6D64bc2Df84e7dd0069A2111C] |
| [Imports]                | [0x8dD188Ec36084D59948F90213AFCd04429E33c0c] |
| [Errors]                 | [0xC1BD0d9A8863f2318001BC5024c7f5F58a2236F7] |
| [The "new" Keyword]      | [0x4f21e69d0CDE8C21cF82a6b37Dda5444716AFA46] |
| [Minimal Tokens]         | [0x10Ce928030E136EcC74d4a4416Db9b533e3c694D] |
| [ERC-20 Tokens]          | [0x4F333c49B820013e5E6Fe86634DC4Da88039CE50] |
| [ERC-721 Tokens]         | [0x15534ED3d1dBA55148695B2Ba4164F147E47a10c] |

[progress page]: https://docs.base.org/base-learn/progress
[Deploying to a Testnet]: https://docs.base.org/base-learn/docs/deployment-to-testnet/deployment-to-testnet-exercise
[Control Structures]: https://docs.base.org/base-learn/docs/control-structures/control-structures-exercise
[Storage]: https://docs.base.org/base-learn/docs/storage/storage-exercise
[Arrays]: https://docs.base.org/base-learn/docs/arrays/arrays-exercise
[Mappings]: https://docs.base.org/base-learn/docs/mappings/mappings-exercise
[Structs]: https://docs.base.org/base-learn/docs/structs/structs-exercise
[Inheritance]: https://docs.base.org/base-learn/docs/inheritance/inheritance-exercise
[Imports]: https://docs.base.org/base-learn/docs/imports/imports-exercise
[Errors]: https://docs.base.org/base-learn/docs/error-triage/error-triage-exercise
[The "new" Keyword]: https://docs.base.org/base-learn/docs/new-keyword/new-keyword-exercise
[Minimal Tokens]: https://docs.base.org/base-learn/docs/minimal-tokens/minimal-tokens-exercise
[ERC-20 Tokens]: https://docs.base.org/base-learn/docs/erc-20-token/erc-20-exercise
[ERC-721 Tokens]: https://docs.base.org/base-learn/docs/erc-721-token/erc-721-exercise
[0x075eB9Dc52177Aa3492E1D26f0fDE3d729625d2F]: https://sepolia.basescan.org/address/0x075eb9dc52177aa3492e1d26f0fde3d729625d2f#code#F16#L1
[0xF4D953A3976F392aA5509612DEfF395983f22a84]: https://sepolia.basescan.org/address/0xf4d953a3976f392aa5509612deff395983f22a84#code#F17#L1
[0x567452C6638c0D2D9778C20a3D59749FDCaa7aB3]: https://sepolia.basescan.org/address/0x567452c6638c0d2d9778c20a3d59749fdcaa7ab3#code#F17#L1
[0x5B0F80cA6f5bD60Cc3b64F0377f336B2B2A56CdF]: https://sepolia.basescan.org/address/0x5b0f80ca6f5bd60cc3b64f0377f336b2b2a56cdf
[0xD32E3ACe3272e2037003Ca54CA7E5676f9b8D06C]: https://sepolia.basescan.org/address/0xd32e3ace3272e2037003ca54ca7e5676f9b8d06c#code#F17#L1
[0x9eB1Fa4cD9bd29ca2C8e72217a642811c1F6176d]: https://sepolia.basescan.org/address/0x9eb1fa4cd9bd29ca2c8e72217a642811c1f6176d#code#F17#L1
[0xF90dA05e77a33Fe6D64bc2Df84e7dd0069A2111C]: https://sepolia.basescan.org/address/0xF90dA05e77a33Fe6D64bc2Df84e7dd0069A2111C#code#F17#L1
[0x8dD188Ec36084D59948F90213AFCd04429E33c0c]: https://sepolia.basescan.org/address/0x8dd188ec36084d59948f90213afcd04429e33c0c#code#F17#L1
[0xC1BD0d9A8863f2318001BC5024c7f5F58a2236F7]: https://sepolia.basescan.org/address/0xc1bd0d9a8863f2318001bc5024c7f5f58a2236f7#code#F17#L1
[0x4f21e69d0CDE8C21cF82a6b37Dda5444716AFA46]: https://sepolia.basescan.org/address/0x4f21e69d0cde8c21cf82a6b37dda5444716afa46#code#F17#L1
[0x10Ce928030E136EcC74d4a4416Db9b533e3c694D]: https://sepolia.basescan.org/address/0x10ce928030e136ecc74d4a4416db9b533e3c694d#code#F17#L1
[0x4F333c49B820013e5E6Fe86634DC4Da88039CE50]: https://sepolia.basescan.org/address/0x4f333c49b820013e5e6fe86634dc4da88039ce50#code#F21#L1
[0x15534ED3d1dBA55148695B2Ba4164F147E47a10c]: https://sepolia.basescan.org/address/0x15534ed3d1dba55148695b2ba4164f147e47a10c#code#F18#L1



<!-- File: ../web/apps/base-docs/base-learn/docs/ethereum-virtual-machine/evm-diagram.md -->

---
title: EVM Diagram
description: An overview of the Ethereum Virtual Machine
hide_table_of_contents: false
---

In this article, we'll examine the inner workings of the EVM, its components, and its role within the Ethereum network.

---

## Objectives

By the end of this lesson you should be able to:

- Diagram the EVM

---

## What is the EVM?

The Ethereum Virtual Machine (EVM) is the core engine of Ethereum. It is a Turing-complete, sandboxed virtual machine designed to execute smart contracts on the network. The term "sandboxed" means that the EVM operates in an isolated environment, ensuring that each smart contract's execution does not interfere with others or the underlying blockchain. As we've learned, the EVM's Turing-complete nature allows developers to write complex programs that can perform any computationally feasible task.

The EVM employs a sophisticated resource management system using gas to regulate computation costs and prevent network abuse. It also supports a rich ecosystem of apps by providing a versatile set of opcodes for smart contract logic, and fostering interoperability with various programming languages, tools, and technologies. This adaptability has made the EVM a fundamental component in the advancement and growth of the Ethereum network.

---

## EVM Components

The EVM has several key components that enable it to process and manage smart contracts. Let's define them:

- **World State:** Represents the entire Ethereum network, including all accounts and their associated storage.
- **Accounts:** Entities that interact with the Ethereum network, including Externally Owned Accounts (EOAs) and Contract Accounts.
- **Storage:** A key-value store associated with each contract account, containing the contract's state and data.
- **Gas:** A mechanism for measuring the cost of executing operations in the EVM, which protects the network from spam and abuse.
- **Opcodes:** Low-level instructions that the EVM executes during smart contract processing.
- **Execution Stack:** A last-in, first-out (LIFO) data structure for temporarily storing values during opcode execution.
- **Memory:** A runtime memory used by smart contracts during execution.
- **Program Counter:** A register that keeps track of the position of the next opcode to be executed.
- **Logs:** Events emitted by smart contracts during execution, which can be used by external systems for monitoring or reacting to specific events.

---

## EVM Execution Model

In simple terms, when a transaction is submitted to the network, the EVM first verifies its validity. If the transaction is deemed valid, the EVM establishes an execution context that incorporates the current state of the network and processes the smart contract's bytecode using opcodes. As the EVM runs the smart contract, it modifies the blockchain's world state and consumes gas accordingly. However, if the transaction is found to be invalid, it will be dismissed by the network without further processing. Throughout the smart contract's execution, logs are generated that provide insights into the contract's performance and any emitted events. These logs can be utilized by external systems for monitoring purposes or to respond to specific events.

![EVM Execution Model](../../assets/images/ethereum-virtual-machine/evm-execution-basic.png)

---

## Gas and Opcode Execution

While we have already delved into the concept of gas in a previous lesson, it is worth reiterating its critical role within the EVM and as a fundamental component of Ethereum. Gas functions as a metric for quantifying the computational effort needed to carry out operations in the EVM. Every opcode in a smart contract carries a specific gas cost, which reflects the computational resources necessary for its execution.

Opcodes are the low-level instructions executed by the EVM. They represent elementary operations that allow the EVM to process and manage smart contracts.

![Opcode Execution](../../assets/images/ethereum-virtual-machine/opcode-execution.png)

During execution, the EVM reads opcodes from the smart contract, and depending on the opcode, it may update the world state, consume gas, or revert the state if an error occurs. Some common opcodes include:

- **ADD:** Adds two values from the stack.
- **SUB:** Subtracts two values from the stack.
- **MSTORE:** Stores a value in memory.
- **SSTORE:** Stores a value in contract storage.
- **CALL:** Calls another contract or sends ether.

---

## Stack and Memory

The EVM stack and memory are critical components of the EVM architecture, as they enable smart contracts to manage temporary data during opcode execution. The stack is a last-in, first-out (LIFO) data structure that is used for temporarily storing values during opcode execution. It is managed by the EVM and is separate from the contract's storage. The stack supports two primary operations: push and pop.

The push operation adds a value to the top of the stack, while the pop operation removes the top value from the stack. These operations are used to manage temporary data during opcode execution. For example, an opcode that performs an addition operation might push the two operands onto the stack, perform the addition, and then pop the result off the top of the stack.

During contract execution, memory serves as a collection of bytes, organized in an array, for the purpose of temporarily storing data. It can be read from and written to by opcodes. Memory is often used to store temporary data during opcode execution, such as when working with dynamically sized data like strings or arrays that are being manipulated or computed within the smart contract before being stored in the contract's storage. When a smart contract needs to store temporary data during opcode execution, it can use the memory to store that data.

![EVM Stack and Memory](../../assets/images/ethereum-virtual-machine/evm-stack-memory.png)

---

## EVM Architecture and Execution Context

To fully grasp the EVM architecture and its components, it's important to see how they all come together in a cohesive manner. The following diagram provides an in-depth visualization of the EVM architecture, showcasing the interactions between key elements such as transactions, gas, opcodes, and the world state. With this diagram, you can see how each component plays a vital role in the seamless execution of smart contracts on the Ethereum network.

![Figure 13-1. EVM architecture and execution context.](../../assets/images/ethereum-virtual-machine/evm-architecture-execution.png)
Image Source: [Mastering Ethereum](https://github.com/ethereumbook/ethereumbook) by Andreas M. Antonopoulos and Gavin Wood, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Conclusion

The EVM plays a vital role within the Ethereum network. By examining the EVM's key components as well as its architecture and execution model, we've gained insight into the engine of Ethereum and how it enables the smooth execution of smart contracts on the platform.

---

## See Also

- [The Ethereum Virtual Machine (Mastering Ethereum)](https://cypherpunks-core.github.io/ethereumbook/13evm.html#evm_architecture)
- [Ethereum Virtual Machine (Ethereum docs)](https://ethereum.org/en/developers/docs/evm/)

<!-- Reference Style Links -->

[the ethereum virtual machine (mastering ethereum)]: https://cypherpunks-core.github.io/ethereumbook/13evm.html#evm_architecture



<!-- File: ../web/apps/base-docs/base-learn/docs/address-and-payable/address-and-payable.md -->

---
title: Address and Payable in Solidity
description: A comprehensive guide to understanding and using address and payable address types in Solidity.
hide_table_of_contents: false
---

Understanding address and payable address types is crucial for managing Ether transfers and interactions within your Solidity contracts. This article will delve into their key distinctions and practical applications.

---

## Objectives

By the end of this lesson, you should be able to:

- Differentiate between address and address payable types in Solidity
- Determine when to use each type appropriately in contract development
- Employ address payable to send Ether and interact with payable functions

---

## Ethereum Addresses

In Solidity, Ethereum addresses play a crucial role in interacting with the Ethereum blockchain. An Ethereum address is a 20-byte hexadecimal string that represents the destination of transactions or the owner of a smart contract. These addresses are used to send and receive Ether and interact with smart contracts.

### Addresses

Regular addresses in Solidity are used for various purposes, including:

- Identifying the owner of a smart contract
- Sending Ether from one address to another
- Checking the balance of an address
  Here's an example of declaring a regular address variable in Solidity:

<br />

```solidity
address public owner;
```

### Payable Addresses

`payable` keyword is a language-level feature provided by Solidity to enable the handling of Ether within smart contracts, and it is not a feature of the Ethereum Virtual Machine itself, but rather a part of the Solidity language's syntax. They are used when you want a contract to be able to receive Ether from external sources, such as other contracts or user accounts.

Payable addresses are often used when creating crowdfunding or token sale contracts, where users send Ether to the contract's address in exchange for tokens or to fund a project.

Here's an example of declaring a payable address variable in Solidity:

```solidity
address payable public projectWallet;
```

Payable [Address] are marked as payable, which means they can accept incoming Ether transactions. It's important to note that regular addresses cannot receive Ether directly.

## Receiving Ether with Payable Addresses

To receive Ether in a contract using a payable address, you need to define a payable function that can accept incoming transactions. This function is typically named receive or fallback. Here's an example:

```solidity
fallback() external payable {
    // Handle the incoming Ether here
}
```

In this example, the fallback function is marked as external and payable, which means it can receive Ether when someone sends it to the contract's address. You can then add custom logic to handle the received Ether, such as updating contract balances or triggering specific actions.

## Usage

```solidity
contract PaymentReceiver {
    address payable owner;

    constructor() payable {
        owner = payable(msg.sender); // Convert msg.sender to payable
    }

    function receiveEther() public payable {
        // This function can receive Ether
    }

    function withdrawEther() public {
        owner.transfer(address(this).balance); // Send Ether to owner
    }
}
```

## Conclusion

Appropriately using address and address payable types is essential for secure and efficient Solidity contract development. By understanding their distinctions and applying them correctly, you can effectively manage Ether transfers and interactions within your contracts.

[Address]: https://docs.soliditylang.org/en/latest/types.html#address



<!-- File: ../web/apps/base-docs/base-learn/docs/welcome.md -->

---
title: Learn to Build Smart Contracts and Onchain Apps
description: Base Learn is a comprehensive, free guide to learning smart contract and onchain app development.
keywords:
  [
    Smart contract development,
    Onchain app development,
    Solidity programming,
    EVM-compatible chains,
    Base blockchain,
    Ethereum smart contracts,
    Learn smart contract development,
    Deploy smart contracts on Base,
  ]
hide_table_of_contents: false
image: /img/base-learn-open-graph.png
---

![Welcome](../assets/images/welcome/Base_Learn_Hero.png)

## Introduction

Welcome to Base Learn, your guide to learning smart contract development. Base Learn's curriculum has been expertly crafted to equip you with the skills and knowledge needed to build and deploy smart contracts on Base, or any EVM-compatible chain, including Ethereum, Optimism, and many more. Plus, you'll be eligible to earn NFTs as you complete each module, showcasing your mastery of the material.

Whether you're a curious novice or a seasoned pro looking to stay ahead of the game, our dynamic lessons cater to all levels of experience. You can start with the basics and work your way up, or dive straight into the more advanced concepts and push your limits to new heights.

Begin your journey today!

## What you can learn in this program

Base Learn covers the following topics. If you're looking for quickstarts, or deeper guides on advanced topics, check out our [Base Builder Tutorials]!

import LearningObjectives from './learning-objectives.md';

<LearningObjectives />

[Base Builder Tutorials]: https://docs.base.org/tutorials/



<!-- File: ../web/apps/base-docs/base-learn/docs/imports/imports-vid.md -->

---
title: Imports
description: Import libraries and contracts into your own contracts.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='817805618' title='Imports' />



<!-- File: ../web/apps/base-docs/base-learn/docs/imports/imports-sbs.md -->

---
title: Imports
description: Learn to import code into your contract.
hide_table_of_contents: false
---

In this lesson, we'll learn how to import code written by others into your contracts. We'll also explore the [OpenZeppelin] library of smart contracts.

---

## Objectives

By the end of this lesson you should be able to:

- Import and use code from another file
- Utilize OpenZeppelin contracts within Remix

---

## OpenZeppelin

[OpenZeppelin] has a robust [library] of well-[documented] smart contracts. These include a number of standard-compliant token implementations and a suite of utilities. All the contracts are audited and are therefore safer to use than random code you might find on the internet (you should still do your own audits before releasing to production).

### Docs

The [docs] start with installation instructions, which we'll return to when we switch over to local development. You do **not** need to install anything to use these contracts in Remix.

Find the documentation for the `EnumerableSet` under _Utils_. This library will allow you to create [sets] of `bytes32`, `address`, and `uint256`. Since they're enumerated, you can iterate through them. Neat!

### Implementing the OpenZeppelin EnumerableSet

Create a new file to work in and add the `pragma` and license identifier.

In Remix, you can import libraries directly from Github!

```solidity
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/structs/EnumerableSet.sol";
```

You should see `EnumerableSet.sol` pop into your workspace files, nested deeply in a bunch of folders.

### Trying It Out

Add a contract called `SetExploration`. Review the extensive comments within the contract itself.

To use the `EnumerableSet`, you need to use the [`using`] keyword. This directive attaches all of the library methods to the type. Doing so allows you to call the method on the variable with dot notation, and the variable itself will be supplied as the first argument.

Follow the pattern in the example in the comments, but name the variable `visitors`:

```
using EnumerableSet for EnumerableSet.AddressSet;

EnumerableSet.AddressSet private visitors;
```

Add a function called `registerVisitor` that makes use of the library's `add` function to add the sender of the message to the `visitors` set.

:::tip

There's also an `_add` function, which is private.

:::

<details>

<summary>Reveal code</summary>

```solidity
function registerVisitor() public {
    visitors.add(msg.sender);
}
```

</details>

<br/>

Add another function to return the `numberOfVisitors`. Thanks to `using`, this can cleanly call the `length` function:

<details>

<summary>Reveal code</summary>

```solidity
function numberOfVisitors() public view returns (uint) {
    return visitors.length();
}
```
</details>

---

## Conclusion

In this lesson, you imported a library from [OpenZeppelin] and implemented some of its functions. You also learned how to use the `using` keyword.

---

[OpenZeppelin]: https://www.openzeppelin.com/
[library]: https://github.com/OpenZeppelin/openzeppelin-contracts
[documented]: https://docs.openzeppelin.com/contracts/4.x/
[docs]: https://docs.openzeppelin.com/contracts/4.x/
[sets]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)
[`using`]: https://docs.soliditylang.org/en/v0.8.17/contracts.html#using-for



<!-- File: ../web/apps/base-docs/base-learn/docs/imports/imports-exercise.md -->

---
title: Imports Exercise
description: Exercise - Demonstrate your knowledge of imports.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a contract called `ImportsExercise`. It should `import` a copy of `SillyStringUtils`

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

library SillyStringUtils {

    struct Haiku {
        string line1;
        string line2;
        string line3;
    }

    function shruggie(string memory _input) internal pure returns (string memory) {
        return string.concat(_input, unicode" 🤷");
    }
}
```

Add a public instance of `Haiku` called `haiku`.

Add the following two functions.

### Save Haiku

`saveHaiku` should accept three strings and save them as the lines of `haiku`.

### Get Haiku

`getHaiku` should return the haiku as a `Haiku` type.

:::info

Remember, the compiler will automatically create a getter for `public` `struct`s, but these return each member individually. Create your own getters to return the type.

:::

### Shruggie Haiku

`shruggieHaiku` should use the library to add 🤷 to the end of `line3`. It must **not** modify the original haiku. It should return the modified `Haiku`.

---

## Submit your Contract and Earn an NFT Badge! (BETA)

:::caution

#### Contract Verification Best Practices

To simplify the verification of your contract on a blockchain explorer like BaseScan.org, consider these two common strategies:

1. **Flattening**: This method involves combining your main contract and all of its imported dependencies into a single file. This makes it easier for explorers to verify the code since they only have to process one file.

2. **Modular Deployment**: Alternatively, you can deploy each imported contract separately and then reference them in your main contract via their deployed addresses. This approach maintains the modularity and readability of your code. Each contract is deployed and verified independently, which can facilitate easier updates and reusability.

3. **Use Desktop Tools**: Forge and Hardhat both have tools to write scripts that both deploy and verify your contracts.

:::

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={19}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/storage/simple-storage-sbs.md -->

---
title: Storing Data
description: Learn how to Store data on the blockchain.
hide_table_of_contents: false
---

Ultimately, the power of the blockchain is that anyone can store their data on it via the `storage` in a smart contract. In this step-by-step guide, you'll learn how to access and use the `storage` data location.

---

## Objectives

By the end of this lesson you should be able to:

- Use the constructor to initialize a variable
- Access the data in a public variable with the automatically generated getter
- Order variable declarations to use storage efficiently

---

## Simple Storage Contract

Create a contract called `SimpleStorage`.

### Add a Storage Variable

In Solidity, variables declared at the class level are automatically `storage` variables. Create a variable to store the age of a person and another to store the number of cars that they own. Give `age` an initial value of your choosing, but don't make an assignment for `cars`;

<details>

<summary>Reveal code</summary>

```solidity
contract SimpleStorage {
    uint8 age = 41;
    uint8 cars;
}
```

</details>

<br/>

Because the age of a person, or the number of cars they own, is unlikely to be greater than 255, we can use a `uint8` for each of these. For types that are smaller than 32 bytes, multiple variables of the same type will be [packed] in the same storage slot. For this to work, the variables must be declared together.

```solidity
// These variables take advantage of packing
uint8 first;
uint8 second;
uint third;

// These variables DO NOT take advantage of packing and should be reordered
uint8 fourth;
uint fifth;
uint8 sixth;
```

### Initializing a Value with the Constructor

You may add a `constructor` function to your contract. Similar to other languages, this function is called exactly once, when the contract is deployed. The constructor may have parameters, but it does not require them.

You can use the constructor to perform various setup tasks. For example, the constructor for the _ERC-721_ token that is the underlying mechanism for most NFTs uses the constructor to set up the name and symbol for the token.

Create a constructor function and use it to assign the value of your choosing to `cars`.

<details>

<summary>Reveal code</summary>

```solidity
constructor() {
    cars = 1;
}
```

</details>

### Accessing State Variables

Deploy your contract in Remix. It should work fine, but you'll have one problem: there isn't a way to see if the variables have the expected values!

You could solve this by writing functions that return the values in your state variables, but you don't need to. The Solidity compiler automatically creates getters for all `public` variables.

Add the `public` keyword to both variables. Unlike most languages, `public` goes **after** the type declaration. Your contract should now be similar to:

<details>

<summary>Reveal code</summary>

```solidity
contract SimpleStorage {
    uint8 public age = 41;
    uint8 public cars;
    constructor() {
        cars = 1;
    }
}
```

</details>

<br/>

Redeploy your contract and test to confirm.

---

## Setting a State Variable with a Function

Good news! Our user bought a second car! The only problem is that we don't have a way to update the number of `cars` stored.

### Add a Function to Update `cars`

Before writing the function, let's think about design considerations for this feature. At any point in time, a user could:

- Buy or otherwise acquire a new car
- Get several new cars all at once (Woohoo!)
- Sell or give away one or more cars (😞)

Given this wide variety of conditions, **a** good approach would be to handle calculating the correct number of cars on the front end, and passing the updated value to the back end.

To meet this need, we can write a `public` function that takes a `uint8` for `_numberOfCars` and then simply assigns that value to the state variable `cars`. Because this function modifies state, it **does not** need `pure` or `view`. It isn't either of those.

<details>

<summary>Reveal code</summary>

```solidity
function updateNumberOfCars(uint8 _numberOfCars) public {
    cars = _numberOfCars;
}
```

</details>

<br/>

Deploy and test to make sure it works as expected.

:::warning

While packing variables can save on gas costs, it can also increase them. The EVM operates on 32 bytes at a time, so it will take additional steps to reduce the size of the element for storage.

Furthermore, the savings in writing to storage only apply when writing multiple values in the same slot at the same time.

Review the **Warning** in the [layout] section of the docs for more details!

:::

### Add a Function to Update `age`

It would also be good to be able to update the `age` value. This problem has slightly different considerations. Sadly, `age` will never go down. It should also probably only go up by one year for each update. The `++` operator works in Solidity, so we can use that to create a function that simple increments age when called.

<details>

<summary>Reveal code</summary>


```solidity
function increaseAge() public {
    age++;
}
```

</details>

<br/>


But what if a user calls this function by mistake? Good point!

On your own, add a function called `adminSetAge` that can set the `age` to a specified value.

### Refactor the Constructor to Accept Arguments

We've got one problem remaining with this contract. What if your user has a different `age` or number of `cars` than what you've hardcoded into the contract?

As mentioned above, the `constructor` **can** take arguments and use them during deployment. Let's refactor the contract to set the two state variables in the constructor based on provided values.

<details>

<summary>Reveal code</summary>

```solidity
contract SimpleStorage {
    uint8 public age;
    uint8 public cars;
    constructor(uint8 _age, uint8 _cars) {
        age = _age;
        cars = _cars;
    }
}
```

</details>

<br/>

Redeploy your contract. Note that now you have added parameters to the `constructor`, you'll have to provide them during deployment.

![Deployment](../../assets/images/storage/deployment-with-params.png)

Once completed, your contract should be similar to:


<details>

<summary>Reveal code</summary>

```solidity
contract SimpleStorage {
    uint8 public age;
    uint8 public cars;
    constructor(uint8 _age, uint8 _cars) {
        age = _age;
        cars = _cars;
    }

    function updateNumberOfCars(uint8 _numberOfCars) public {
        cars = _numberOfCars;
    }

    function increaseAge() public {
        age++;
    }

    function adminSetAge(uint8 _age) public {
        age = _age;
    }
}
```

</details>

<br/>

---

## Conclusion

In this lesson, you've explored how to persistently store values on the blockchain. You've also practiced updating them from functions. Finally, you've learned how to use the constructor to perform setup functionality during deployment, with and without parameters.

---

[packed]: https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html
[layout]: https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html



<!-- File: ../web/apps/base-docs/base-learn/docs/storage/how-storage-works.md -->

---
title: How Storage Works
description: An introduction to how storage works in Ethereum
hide_table_of_contents: false
---

In this article, we will delve into the workings of Ethereum storage, explore the nuances of variable declaration ordering, and provide examples of efficient and inefficient storage practices to create optimized smart contracts.

---

## Objectives:

By the end of this lesson you should be able to:

- Diagram how a contract's data is stored on the blockchain (Contract -> Blockchain)
- Order variable declarations to use storage efficiently
- Diagram how variables in a contract are stored (Variable -> Contract)

---

## Introduction

Creating smart contracts that can operate efficiently requires a thorough understanding of how storage works in Ethereum. When designing a contract, you need to consider the storage requirements of the contract, including the types of storage needed, the gas costs associated with storage operations, and how to manage storage effectively. Poor storage management practices can lead to bloated contracts that consume excessive gas, making them more expensive to execute. By following best practices for storage management, you'll be equipped to create contracts that are lean, efficient, and cost-effective.

---

## Smart Contract Data Storage

### Key-Value Store

Smart contracts on Ethereum store and manage data utilizing a key-value store model, where each piece of data is identified by a unique key and accompanied by its corresponding value.

In this diagram, the keys (user addresses) are unique identifiers used to index the corresponding values (balances):

![Key Value Store](../../assets/images/introduction-to-solidity/key-value-store.png)

This model can be compared to a dictionary or a map where the key serves as the index and the value represents the data associated with that index. However, the key-value store has distinct characteristics that set it apart from these traditional data structures, which make it a more optimal choice for smart contracts on Ethereum.

- **Simplicity:** It is simple and straightforward, which allows for easier implementation and maintenance within a contract.

- **Scalability:** It is highly scalable, making it well-suited for managing vast amounts of data typically associated with apps and smart contracts. This scalability helps maintain performance levels even as data storage requirements grow.

- **Fixed-size chunks:** Storing data in fixed-size 32-byte chunks optimizes storage space and ensures that data location calculations are more efficient. This feature is particularly beneficial in the context of Ethereum, where storage costs are a significant concern.

- **Efficient storage and retrieval:** It is optimized for storing and retrieving large volumes of data efficiently, which is essential for quick access to stored information.

- **Security and immutability:** Unlike other storage models that may allow direct data manipulation, key-value stores within Ethereum's environment ensure data integrity and security through transaction-based modifications. This feature aligns with the decentralized and trustless nature of blockchain technology.

- **Gas-efficiency:** In Ethereum, every operation within a smart contract execution consumes gas. The key-value store model is designed to be gas-efficient, minimizing the gas consumption for storage and retrieval operations, thus reducing the overall cost of contract execution.

- **Compatibility with decentralized environments:** It is particularly suitable for decentralized environments, where data consistency, integrity, and security are crucial. The model's design inherently addresses the challenges posed by multi-threaded or concurrent environments where multiple processes or functions may attempt to access or modify the same data simultaneously.

### Types of Storage

There are three primary types of storage in Ethereum smart contracts: storage, memory, and stack. Each type has its specific use case and characteristics, which make them suitable for different aspects of smart contract execution.

#### Storage

Storage is the most persistent and expensive form of data storage. Data stored in the contract's storage persists across transaction executions and is accessible to any function within the smart contract. This storage is also visible on the blockchain and can be read by external sources, making it suitable for storing important and long-lasting information related to the contract's state.

Key attributes of storage:

- **Persistent:** Data remains in storage even after the contract execution finishes, allowing for state continuity across multiple transactions.

- **Expensive:** Storing and modifying data in storage consumes more gas compared to other data locations, making it costly in terms of transaction fees.

- **Visible on the blockchain:** Storage data is publicly available and can be read by external parties.

Consider the following contract:

```solidity
contract StorageDemo {
    // Declare a state variable to store data in storage
    uint256 public storedData;

    // Function to update the storedData variable in storage
    function updateData(uint256 newData) public {
        storedData = newData;
    }
}
```

The contract includes a state variable called `storedData`, which is stored in the contract's storage. The `public` visibility modifier allows anyone to access this variable. The contract also includes a public function called `updateData`, which can be called by anyone to modify the value of `storedData` in storage.

Any changes made to `storedData` in storage will persist across multiple transactions and will be visible to anyone who reads the blockchain. Please note that storage is more expensive than other data locations, so it is important to use it judiciously to minimize gas costs.

#### Memory

Memory is a temporary and more affordable data location. It's used to save data during the execution of a single transaction. Once the transaction is complete, the memory is wiped clean and any data within it is lost. Memory is suitable for storing intermediate variables and temporary data that does not need to persist across multiple transactions.

Key attributes of memory:

- **Temporary:** Data in memory is only available during a single transaction execution and is lost afterward.

- **Less expensive:** Saving and modifying data in memory consumes less gas compared to storage, making it more cost-effective for temporary data.

- **Not visible on the blockchain:** Memory data is not accessible to external parties and remains confined to the transaction execution.

Consider the following contract:

```solidity
contract MemoryDemo {
    // Declare a state variable to store data in storage
    uint256 public storedData;

    // Function to update the storedData variable in memory
    function updateData(uint256 newData) public {
        // Declare a memory variable to store the new data
        uint256 tempData = newData;

        // Assign the value of the memory variable to the storage variable
        storedData = tempData;
    }
}
```

In the contract, we declare a memory variable called `tempData` and assign the input parameter `newData` to it to update its value. The `tempData` variable is then assigned to the `storedData` variable to update its value in storage.

Unlike storage, data stored in memory is not persisted across transactions and is only accessible during the execution of the function. However, accessing and modifying data in memory is less expensive than doing so in storage, making it a more efficient option when dealing with temporary data. Additionally, any data stored in memory is not visible on the blockchain and cannot be read by external parties.

#### Stack

The stack is another form of temporary data storage, specifically used for holding function arguments, local variables, and intermediate values during function execution. The stack follows a Last-In-First-Out (LIFO) structure, meaning that the most recently added item is the first to be removed. This storage type is highly efficient but has limited space, making it suitable for small-scale data manipulation during function execution.

The stack is an internal data structure used by the EVM (Ethereum Virtual Machine) for computation during the execution of transactions. When a transaction is executed by the EVM, the bytecode of the smart contract is loaded into memory, and the EVM uses the stack to keep track of intermediate results and execute operations.

In Solidity, developers do not interact with the stack directly, but can optimize their code to make the best use of it and minimize the amount of gas used during transaction execution. This can include using more efficient algorithms or data structures, or avoiding unnecessary operations that can increase the depth of the stack.

Key attributes of the stack:

- **Temporary:** Like memory, stack data is only available during a single transaction execution and is lost afterward.

- **Highly efficient:** Stack operations consume minimal gas, making it the most cost-effective storage option for small-scale data manipulation.

- **LIFO structure:** The stack follows the Last-In-First-Out order, which allows for efficient management of function arguments, local variables, and intermediate values.

- **Limited space:** The stack has a maximum depth of 1024, restricting the number of elements it can hold at a given time.

- **Limited visibility:** Only the top 16 elements in the stack are accessible, limiting how many variables and other elements can be in scope at one time.

Let's compare two versions of a function and analyze their gas efficiency with regard to stack usage and gas consumption:

```solidity
contract GasEfficiencyDemo {
    uint256 public result;

    // Less efficient
    function sumLessEfficient(uint256 a, uint256 b) public {
        uint256 temp = a + b;
        result = temp;
    }

    // More efficient
    function sumMoreEfficient(uint256 a, uint256 b) public {
        result = a + b;
    }
}
```

In the `sumLessEfficient` function, the sum of the two input arguments `a` and `b` is first assigned to the temporary variable `temp` before being assigned to the state variable `result`. This additional step introduces an extra variable on the stack, which requires more gas for stack operations and consumes more gas overall.

In contrast, the `sumMoreEfficient` function directly assigns the sum of the input arguments `a` and `b` to the state variable result. This eliminates the need for the temporary variable and reduces the stack usage, leading to lower gas consumption for stack operations and a more gas-efficient execution.

Although the difference in gas consumption between these two functions may not be significant for such a simple example, the principle of minimizing stack usage and optimizing code to reduce gas consumption is essential for developing efficient smart contracts. By avoiding unnecessary variables and operations, you can improve the gas efficiency of your functions and reduce the cost of executing them on the EVM.

## Variable Storage

### Variable Packing

As we've learned, minimizing the storage footprint of a contract can substantially reduce gas costs. To make storage more efficient, Ethereum employs a concept called variable packing.

Variable packing is the process of placing multiple smaller variables into a single storage slot to optimize storage usage. A storage slot is a fixed-size container that can hold up to 32 bytes of data. Ethereum's Solidity compiler automatically packs smaller variables together if they can fit into a single storage slot.

![Variable Packing](../../assets/images/introduction-to-solidity/variable-packing.png)

### Ordering Variable Declarations

When declaring variables in a contract, their order can impact a contract's gas usage. You can optimize storage by declaring variables of similar sizes together, such that they can be packed into the same storage slot.

Let's illustrate how this works:

```solidity
contract StoragePackingExample {
    uint8 a; // 1 byte
    uint8 b; // 1 byte
    uint256 c; // 32 bytes
}
```

In this example, the compiler will automatically pack `a` and `b` into the same storage slot, as they are both 1-byte variables and can fit into a single 32-byte storage slot. However, `c` requires a separate storage slot due to its size (32 bytes).

![Variable Order Optimized](../../assets/images/introduction-to-solidity/variable-order-optimized.png)

If these variables were not in the correct order, the contract would not take advantage of variable packing. The variables would take up more storage and would potentially consume more gas to execute the contract.

Let's consider an inefficient example:

```solidity
contract StoragePackingBadExample {
    uint8 a; // 1 byte
    uint256 b; // 32 bytes
    uint8 c; // 1 byte
}
```

In this contract, the variables are not declared in the optimal order, and the compiler would store these variables in the following way:

![Variable Order Inefficient](../../assets/images/introduction-to-solidity/variable-order-inefficient.png)

To make the most of variable packing, it's important to group variables of the same size together and avoid mixing variable sizes. ​By doing this, the compiler can store them more efficiently, reducing the overall storage usage of the contract. This optimization will not only reduce the gas costs associated with storage, but it will also improve the contract's execution speed.

---

## Conclusion

Creating efficient and optimized smart contracts on Ethereum requires a thorough understanding of how storage works. Smart contracts use a key-value store model to manage and store data, which is simple, scalable, gas-efficient, and suitable for decentralized environments. There are three types of storage in Ethereum smart contracts: storage, memory, and stack, each with specific characteristics. Developers can optimize storage usage by using variable packing and ordering variable declarations based on their size. By following best practices for storage management, developers can create contracts that are lean, efficient, cost-effective, and improve their execution speed.

---

## See Also

- [Understanding Ethereum Smart Contract Storage](https://programtheblockchain.com/posts/2018/03/09/understanding-ethereum-smart-contract-storage/)
- [What is Smart Contract Storage Layout](https://docs.alchemy.com/docs/smart-contract-storage-layout)

<!-- Reference Style Links -->

[ethereum in depth, part 2]: https://blog.openzeppelin.com/ethereum-in-depth-part-2-6339cf6bddb9/
[ethereum yellow paper]: https://ethereum.github.io/yellowpaper/paper.pdf



<!-- File: ../web/apps/base-docs/base-learn/docs/storage/storage-exercise.md -->

---
title: Storage Exercise
description: Exercise - Demonstrate your knowledge of storage.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications:

---

## Contract

Create a single contract called `EmployeeStorage`. It should not inherit from any other contracts. It should have the following functions:

### State Variables

The contract should have the following state variables, optimized to minimize storage:

- A private variable `shares` storing the employee's number of shares owned
  - Employees with more than 5,000 shares count as directors and are stored in another contract
- Public variable `name` which stores the employee's name
- A private variable `salary` storing the employee's salary
  - Salaries range from 0 to 1,000,000 dollars
- A public variable `idNumber` storing the employee's ID number
  - Employee numbers are not sequential, so this field should allow any number up to 2^256-1

### Constructor

When deploying the contract, utilize the `constructor` to set:

- `shares`
- `name`
- `salary`
- `idNumber`

For the purposes of the test, you **must** deploy the contract with the following values:

- `shares` - 1000
- `name` - Pat
- `salary` - 50000
- `idNumber` - 112358132134

### View Salary and View Shares

:::danger

In the world of blockchain, nothing is ever secret!\* `private` variables prevent other contracts from reading the value. You should use them as a part of clean programming practices, but marking a variable as private **does _not_ hide the value**. All data is trivially available to anyone who knows how to fetch data from the chain.

\*You can make clever use of encryption though!

:::

Write a function called `viewSalary` that returns the value in `salary`.

Write a function called `viewShares` that returns the value in `shares`.

### Grant Shares

Add a public function called `grantShares` that increases the number of shares allocated to an employee by `_newShares`. It should:

- Add the provided number of shares to the `shares`
  - If this would result in more than 5000 shares, revert with a custom error called `TooManyShares` that returns the number of shares the employee would have with the new amount added
  - If the number of `_newShares` is greater than 5000, revert with a string message, "Too many shares"

### Check for Packing and Debug Reset Shares

Add the following function to your contract exactly as written below.

```solidity
/**
* Do not modify this function.  It is used to enable the unit test for this pin
* to check whether or not you have configured your storage variables to make
* use of packing.
*
* If you wish to cheat, simply modify this function to always return `0`
* I'm not your boss ¯\_(ツ)_/¯
*
* Fair warning though, if you do cheat, it will be on the blockchain having been
* deployed by your wallet....FOREVER!
*/
function checkForPacking(uint _slot) public view returns (uint r) {
    assembly {
        r := sload (_slot)
    }
}

/**
* Warning: Anyone can use this function at any time!
*/
function debugResetShares() public {
    shares = 1000;
}
```

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={3}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/storage/how-storage-works-video.md -->

---
title: How Storage Works
description: Learn how storage works in the EVM.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479654' title='How Storage Works' />



<!-- File: ../web/apps/base-docs/base-learn/docs/storage/simple-storage-video.md -->

---
title: Simple Storage
description: Store data on the blockchain.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479707' title='Simple Storage' />



<!-- File: ../web/apps/base-docs/base-learn/docs/intro-to-tokens/misconceptions-about-tokens-vid.md -->

---
title: Common Misconceptions
description: Review some common misconceptions before starting.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='808096842' title='Misconceptions About Tokens' />



<!-- File: ../web/apps/base-docs/base-learn/docs/intro-to-tokens/intro-to-tokens-vid.md -->

---
title: Introduction
description: Welcome to the wonderful world of tokens!
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='808096827' title='Introduction to Tokens' />



<!-- File: ../web/apps/base-docs/base-learn/docs/intro-to-tokens/tokens-overview.md -->

---
title: Overview
description: An overview of tokens on Ethereum
hide_table_of_contents: false
---

This article will provide an overview of the most popular token standards on Ethereum, including ERC-20, ERC-721, ERC-1155, and a discussion on their properties and various use cases.

---

## Objectives:

By the end of this lesson you should be able to:

- Describe the properties of ERC-20 and ERC-721 tokens
- List popular ERC-721 tokens
- List the uses for ERC-20, ERC-721, and ERC-1155 tokens

---

## ERC Token Standards

Ethereum Request for Comments (or, ERC) is a term used to describe technical proposals and standards for Ethereum. An ERC is authored by developers and members of the Ethereum community to suggest improvements, new features, or guidelines for creating and managing tokens and smart contracts. Once an ERC is submitted, it undergoes review and discussion by the community. If it gains consensus, it can then be implemented or adopted as a standard in the ecosystem.

Token standards on Ethereum form the backbone of the digital asset ecosystem. They are a set of predefined rules and guidelines that govern the creation, management, and interaction of tokens on the network. These standards ensure that tokens are compatible with various apps, wallets, and other tokens within the Ethereum ecosystem. Token standards allow developers to create tokens with consistent behavior, facilitating seamless interaction and interoperability within the network.

---

## ERC-20

ERC-20 tokens, the most widely-used token standard on Ethereum, possess several key properties that make them versatile and flexible for various applications. One of the defining characteristics of these tokens is their fungibility. Each unit of an ERC-20 token is interchangeable and holds equal value to another unit of the same token, rendering them indistinguishable from one another. In other words, one USDC token is always equal in value and interchangeable with another USDC token.

Another aspect of ERC-20 tokens is their standardized interface, which includes a set of six mandatory functions: `totalSupply()`, `balanceOf(address)`, `transfer(address, uint256)`, `transferFrom(address, address, uint256)`, `approve(address, uint256)`, and `allowance(address, address)`. This standardization ensures consistency when interacting with these tokens, irrespective of their specific implementation or use case. For example, a user can easily check their token balance or transfer tokens using the same set of functions, whether they are interacting with a governance token like UNI or a stablecoin like DAI.

Some notable applications of ERC-20 tokens include utility tokens (FIL, BAT, MANA), governance tokens (UNI, AAVE, COMP), and stablecoins (USDC, USDT, DAI).

![Properties of ERC-20 Token](../../assets/images/introduction-to-tokens/erc-20.png)

---

## ERC-721

ERC-721 is a prominent token standard specifically designed for NFTs, allowing for the creation and management of unique, indivisible digital assets that each have their own special properties.

In contrast to ERC-20 tokens, which are fungible and can be easily exchanged, ERC-721 tokens are non-fungible and can't be swapped on a one-to-one basis. Every token has its own attributes that set it apart from the rest. This one-of-a-kind nature enables the representation of a wide range of digital assets, including digital art, virtual real estate, and collectibles. For example, an artist could mint a one-of-a-kind digital painting, a virtual land parcel could be tokenized in a metaverse, or a rare sports card could be digitized as a collectible NFT.

ERC-721 tokens, like ERC-20 tokens, follow a standardized interface but employ a unique set of functions designed for non-fungible tokens, which allow developers to interact with NFTs across multiple platforms. For instance, a developer would use the same set of functions to interact with a digital artwork NFT listed on OpenSea as they would with a virtual land parcel NFT in Decentraland.

Besides their unique qualities, ERC-721 tokens come with metadata properties that offer information about the token's specific features, such as the artwork's title, the artist, and an image preview. This metadata helps users better understand and appreciate the distinct aspects of each NFT, and it is consistent across platforms.

Some notable applications of ERC-721 tokens include digital art by Beeple, virtual collectibles by NBA Top Shot, virtual real estate in Decentraland, and Ethereum-based domain names like vitalik.eth on the Ethereum Name Service (ENS).

![Properties of ERC-721 Token](../../assets/images/introduction-to-tokens/erc-721.png)

---

## ERC-1155

ERC-1155 is an innovative hybrid token standard that merges the best aspects of both fungible and non-fungible tokens, enabling developers to create and manage diverse token types using a single smart contract. This combination of features allows ERC-1155 tokens to provide greater versatility while representing a wide array of assets with different levels of fungibility.

For example, a video game might use both fungible and non-fungible tokens within its ecosystem. Fungible tokens could represent in-game currencies, consumables, or resources, while non-fungible tokens could represent exclusive and unique items like character skins, weapons, or collectible cards.

Digital artists can also benefit from ERC-1155, as it allows them to mint limited edition series of their artwork, with each piece in the series having unique attributes. At the same time, they can create fungible tokens that represent ownership of a specific edition number within the series.

Similar to other token standards, ERC-1155 tokens adhere to a standardized interface with a set of functions that ensure consistency and compatibility across platforms and services. Furthermore, this standard enables efficient batch transfers, simplifying the process and reducing the cost of managing multiple tokens within a single application. For instance, a user who has collected various in-game items in a virtual world can leverage ERC-1155's batch transfer feature to send multiple fungible and non-fungible tokens to another user or marketplace simultaneously. This efficient approach minimizes transaction costs and the complexity typically involved in transferring numerous tokens one by one.

![Properties of ERC-1155 Token](../../assets/images/introduction-to-tokens/erc-1155.png)

---

## Other Token Standards

In addition to the three most prominent token standards that we covered, it is worth mentioning that other standards like ERC-777 and ERC-4626 have been introduced to address specific use cases or challenges. ERC-777 offers enhanced security and functionality over the fungible ERC-20 standard, while ERC-4626 streamlines yield-bearing vault integration by optimizing and unifying technical parameters. These lesser-known standards highlight the ongoing innovation and adaptability of the Ethereum token ecosystem as it continues to grow and evolve.

---

## Conclusion

Ethereum's ERC token standards have played a pivotal role in shaping the digital asset ecosystem by providing clear guidelines and rules for the creation, management, and interaction of tokens on the network. From the widely-used ERC-20 standard for fungible tokens to the distinct ERC-721 standard for non-fungible tokens and the versatile hybrid ERC-1155 standard, these token standards empower developers to craft diverse tokens tailored to various use cases and applications. The standardized interfaces ensure seamless interoperability within the Ethereum ecosystem, facilitating token transfers and interactions across different platforms and services. Additional token standards, such as ERC-777 and ERC-4626, address specific challenges and further demonstrate the continuous innovation and adaptability of the Ethereum token ecosystem.

---

## See Also

- [EIP-20](https://eips.ethereum.org/EIPS/eip-20)
- [EIP-721](https://eips.ethereum.org/EIPS/eip-721)
- [EIP-1155](https://eips.ethereum.org/EIPS/eip-1155)
- [EIP-777](https://eips.ethereum.org/EIPS/eip-777)
- [EIP-4626](https://eips.ethereum.org/EIPS/eip-4626)

<!-- Reference Style Links -->

[token standards]: https://ethereum.org/en/developers/docs/standards/tokens/



<!-- File: ../web/apps/base-docs/base-learn/docs/reading-and-displaying-data/useAccount.md -->

---
title: The `useAccount` Hook
description: Learn how to access information about the connected user's wallet.
hide_table_of_contents: false
---

[wagmi] is a library that provides React hooks that trade a somewhat complex setup process for a great developer experience when building a frontend around the constraints and quirks of onchain building. One of the hooks, `useAccount`, provides access to information about your users' wallet and connection information.

You can use this for connection-status-based rendering, to enable or disable controls or views based on address, and many other useful tasks.

---

## Objectives

By the end of this guide you should be able to:

- Implement the `useAccount` hook to show the user's address, connection state, network, and balance
- Implement an `isMounted` hook to prevent hydration errors

---

## Displaying Connection Information

We'll be working from an app generated by RainbowKit's [quick start]. Either open the one you created when we were exploring [Wallet Connectors], or create a new one for this project.

Either way, change the list of chains to only include `baseSepolia` as the network option. You don't want to accidentally spend real money while developing!

You can set up your providers as described in [Introduction to Providers], or use the default from RainbowKit:

```tsx
const config = getDefaultConfig({
  appName: 'RainbowKit App',
  projectId: 'YOUR APP ID',
  chains: [baseSepolia],
  ssr: true,
});
```

Either way, be sure to set `ssr` to `true`, or you will get a [hydration error] from Next.js.

### The `useAccount` Hook

The [`useAccount`] hook allows you to access account and connection data from within any of your components.

Add a folder for `components` and a file called `ConnectionWindow.tsx` in that folder. Add the below component to the file, and replace the boilerplate text in `index.tsx` with an instance of it.

```tsx
// ConnectionWindow.tsx
export function ConnectionWindow() {
  return (
    <div>
      <p>Connection Status</p>
    </div>
  );
}
```

```tsx
// index.tsx
import { ConnectButton } from '@rainbow-me/rainbowkit';
import type { NextPage } from 'next';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import { ConnectionWindow } from '../components/ConnectionWindow';

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <ConnectButton />
        <ConnectionWindow />
      </main>
    </div>
  );
};

export default Home;
```

For the purposes of this exercise, open `styles/Home.module.css` and **delete or comment out** `.main`. Doing so will move the content to the top of the page, which will prevent the RainbowKit modal from blocking your ability to see changes.

Return to `ConnectionWindow.tsx` and add the `useAccount` hook to the top, where you'd add any state variables. The general pattern for wagmi hooks is you decompose the properties you want to use from a function call of the name of the hook. For some, you'll add a config object to that call, but it's not needed for this one.

```tsx
import { useAccount } from 'wagmi';

export function ConnectionWindow() {
  const { address, isConnected, isConnecting, isDisconnected } = useAccount();

  return (
    <div>
      <h2>Connection Status</h2>
    </div>
  );
}
```

You can see all the deconstructable return options in the [UseAccountReturnType]:

Update your `<div>` to show the address of the connected wallet:

```tsx
<div>
  <h2>Connection Status</h2>
  <div>
    <p>{'Address: ' + address}</p>
  </div>
</div>
```

Test it out by connecting and disconnecting with your wallet. You should see your full address when you are connected, and the address will be `undefined` when you are disconnected.

### Connection Status Conditional Rendering

It isn't very nice to display a value of `undefined` to the user, so let's use the connection status values for conditional rendering depending on if the user is disconnected, connected, or connecting.

A common pattern is to use the conditional directly in the html return of a component or render function. For example, we could add a line to show that we're connecting as demonstrated:

```
<div>
  <h2>Connection Information</h2>
  <div>
    {!isConnecting && <p>Please click Connect in your wallet...</p>}
    <p>{"Address: " + address}</p>
  </div>
</div>
```

Connect and disconnect your wallet a few times. The `isConnecting` state is true while the _Connect to website_ wallet UI is open.

Autoconnect is enabled by default, so you'll need to clear the connection from your wallet settings to see this more than once. Otherwise, it will briefly flash as the autoconnect processes.

Use the `connected` property in the same way to only render the wallet address if there is a wallet connected. Similarly, use the `isDisconnected` property to show a message asking the user to connect.

```
<div>
  <h2>Connection Information</h2>
  <div>
    {isConnecting && <p>Please click Connect in your wallet...</p>}
    {isConnected && <p>{"Address: " + address}</p>}
    {isDisconnected && <p>Please connect your wallet to use this app.</p>}
  </div>
</div>
```

---

## Conclusion

In this guide, you've learned how the `useAccount` hook gives you access to information about the user's connection status and wallet. It can be used in any part of your app that is wrapped by the wagmi context provider. You've also learned a technique for conditional rendering based on connection status. Finally, you've learned to set the `ssr` flag to prevent hydration errors due to the client and server possessing different information about the user's connection status.

---

[RainbowKit]: https://www.rainbowkit.com/
[wagmi]: https://wagmi.sh/
[quick start]: https://www.rainbowkit.com/docs/installation/
[Wallet Connectors]: ../frontend-setup/wallet-connectors/
[`useAccount`]: https://wagmi.sh/react/hooks/useAccount
[hydration error]: https://nextjs.org/docs/messages/react-hydration-error
[Introduction to Providers]: https://docs.base.org/tutorials/intro-to-providers/
[UseAccountReturnType]: https://wagmi.sh/react/api/hooks/useAccount#return-type



<!-- File: ../web/apps/base-docs/base-learn/docs/reading-and-displaying-data/useReadContract.md -->

---
title: The `useReadContract` Hook
description: Learn how to call view and pure functions from a smart contract.
hide_table_of_contents: false
---

The `useReadContract` hook is [wagmi]'s method of calling `pure` and `view` functions from your smart contracts. As with `useAccount`, `useReadContract` contains a number of helpful properties to enable you to manage displaying information to your users.

---

## Objectives

By the end of this guide you should be able to:

- Implement wagmi's `useReadContract` hook to fetch data from a smart contract
- Convert data fetched from a smart contract to information displayed to the user
- Identify the caveats of reading data from automatically-generated getters

---

## Contract Setup

For this guide, you'll be continuing from the project you started for the [`useAccount` hook]. You'll work with an upgrade to the contract that you may have created if you completed the [ERC 20 Tokens Exercise]. See below for an example you can use if you don't already have your own!

The contract creates a very simple DAO, in which users can create issues and vote for them, against them, or abstain. Anyone can `claim` 100 tokens. This is an insecure system for demonstration purposes, since it would be trivial to claim a large number of tokens with multiple wallets, then transfer them to a single address and use that to dominate voting.

But it makes it much easier to test!

:::caution

If you're using your own contract, please redeploy it with the following `view` functions:

```solidity
function numberOfIssues() public view returns(uint) {
    return issues.length;
}

function getAllIssues() public view returns(ReturnableIssue[] memory) {
    ReturnableIssue[] memory allIssues = new ReturnableIssue[](issues.length);

    for(uint i = 0; i < issues.length; i++) {
        allIssues[i] = getIssue(i);
    }

    return allIssues;
}
```

**You also need to make the `getIssue` function `public`. The original spec called for it to be `external`.**

:::

### Create Demo Issues

To start, you'll need to put some data into your contract so that you can read it from your frontend. Open [Sepolia BaseScan], find your contract, connect with your wallet, and call the `claim` function.

Add the following two issues:

```text
_issueDesc: We should enable light mode by default.
_quorum: 2
```

```text
_issueDesc: We should make inverted mouse controls the default selection.
_quorum: 2
```

Switch to a **different wallet address**. Claim your tokens with the new address, and add one more issue:

```text
_issueDesc: Two spaces, not four, not tabs!
_quorum: 2
```

Call the `getAllIssues` function under the `Read Contract` tab to make sure all three are there.

---

## Reading from your Smart Contract

To be able to read from your deployed smart contract, you'll need two pieces of information: the address and [ABI]. These are used as parameters in the `useReadContract` hook.

If you're using [Hardhat], both of these can be conveniently found in a json file in the `deployments/<network>` folder, named after your contract. For example, our contract is called `FEWeightedVoting`, so the file is `deployments/base-sepolia/FEWeightedVoting.json`.

If you're using something else, it should produce a similar artifact, or separate artifacts with the [ABI] and address. If this is the case, make the adjustments you need when you import this data.

Either way, add a folder called `deployments` and place a copy of the artifact file(s) inside.

### Using the `useReadContract` Hook

Add a file for a new component called `IssueList.tsx`. You can start with:

```tsx
import { useReadContract } from 'wagmi';

export function IssueList() {
  return (
    <div>
      <h2>All Issues</h2>
      <div>{/* TODO: List each issue */}</div>
    </div>
  );
}
```

You'll need to do some prepwork to enable Typescript to more easily interpret the data returned from your contract. Add an `interface` called `Issue` that matches with the `ReturnableIssue` type:

```tsx
interface Issue {
  voters: string[];
  issueDesc: string;
  votesFor: bigint;
  votesAgainst: bigint;
  votesAbstain: bigint;
  totalVotes: bigint;
  quorum: bigint;
  passed: boolean;
  closed: boolean;
}
```

:::warning

Be very careful here! `bigint` is the name of the type, `BigInt` is the name of the constructor for that type. If you incorrectly use the constructor as the type, much of your code will still work, but other parts will express very confusing bugs.

:::

Now, import `useState` and add a state variable to hold your list of `Issue`s.

```tsx
const [issues, setIssues] = useState<Issue[]>([]);
```

You'll also need to import your contract artifact:

```tsx
import contractData from '../deployments/FEWeightedVoting.json';
```

Finally, the moment you've been waiting for: Time to read from your contract! Add an instance of the [`useReadContract`] hook. It works similarly to the [`useAccount`] hook. Configure it with:

```tsx
const {
  data: issuesData,
  isError: issuesIsError,
  isPending: issuesIsPending,
} = useReadContract({
  address: contractData.address as `0x${string}`,
  abi: contractData.abi,
  functionName: 'getAllIssues',
});
```

You can use `useEffect` to do something when the call completes and the data. For now, just log it to the console:

```tsx
useEffect(() => {
  if (issuesData) {
    const issuesList = issuesData as Issue[];
    console.log('issuesList', issuesList);
    setIssues(issuesList);
  }
}, [issuesData]);
```

Add in instance of your new component to `index.tsx`:

```tsx
<main className={styles.main}>
  <ConnectButton />
  <ConnectionWindow />
  <IssueList />
</main>
```

Run your app, and you should see your list of issues fetched from the blockchain and displayed in the console!

![Issues Console Log](../../assets/images/reading-and-displaying-data/issues-console-log.png)

Breaking down the hook, you've:

- Renamed the properties decomposed from `useReadContract` to be specific for our function. Doing so is helpful if you're going to read from more than one function in a file
- Configured the hook with the address and ABI for your contract
- Made use of `useEffect` to wait for the data to be returned from the blockchain, log it to the console, and set the list of `Issue`s in state.

### Displaying the Data

Now that you've got the data in state, you can display it via your component. One strategy to display a list of items is to compile a `ReactNode` array in a render function.

```tsx
function renderIssues() {
  return issues.map((issue) => (
    <div key={issue.issueDesc}>
      <h3>{issue.issueDesc}</h3>
      <p>{'Voters: ' + issue.voters.toString()}</p>
      <p>{'Votes For: ' + issue.votesFor.toString()}</p>
      <p>{'Votes Against: ' + issue.votesAgainst.toString()}</p>
      <p>{'Votes Abstain: ' + issue.votesAbstain.toString()}</p>
      <p>{'Quorum: ' + issue.quorum.toString()}</p>
      <p>{'Passed: ' + issue.passed}</p>
      <p>{'Closed: ' + issue.closed}</p>
    </div>
  ));
}
```

Then, call the render function in the return for your component:

```tsx
return (
  <div>
    <h2>All Issues</h2>
    <div>{renderIssues()}</div>
  </div>
);
```

You'll now see your list of issues rendered in the browser! Congrats, you've finally made a meaningful connection between your smart contract and your frontend!

### A Caveat with Automatic Getters

Remember how the Solidity compiler creates automatic getters for all of your public state variables? This feature is very helpful, but it can create bewildering results when you use it for `struct`s that contain `mapping`s. Remember, nesting mappings **cannot** be returned outside the blockchain. The `enumerableSet` protects you from this problem, because it has private variables inside it, which prevents setting `issues` as `public`. Had we instead used a mapping, we'd lose this protection:

```solidity
  // Code for demo only
  struct Issue {
      mapping(address => bool) voters;
      string issueDesc;
      uint votesFor;
      uint votesAgainst;
      uint votesAbstain;
      uint totalVotes;
      uint quorum;
      bool passed;
      bool closed;
  }
```

Redeploy with the above change, and add a second `useReadContract` to fetch an individual issue using the getter:

```tsx
// Bad code for example, do not use
const {
  data: getOneData,
  isError: getOneIsError,
  isPending: getOneIsPending,
} = useReadContract({
  address: contractData.address as `0x${string}`,
  abi: contractData.abi,
  functionName: 'issues',
  args: [1],
});

useEffect(() => {
  if (getOneData) {
    console.log('getOneData', getOneData);
    const issueOne = getOneData as Issue;
    console.log('Issue One', issueOne);
  }
}, [getOneData]);
```

Everything appears to be working just fine, but how is `issueOne.desc` undefined? You can see it right there in the log!

![Missing Data](../../assets/images/reading-and-displaying-data/missing-data.png)

If you look closely, you'll see that `voters` is missing from the data in the logs. What's happening is that because the nested `mapping` cannot be returned outside the blockchain, it simply isn't. TypeScript then gets the `data` and does the best it can to cast it `as` an `Issue`. Since `voters` is missing, this will fail and it instead does the JavaScript trick of simply tacking on the extra properties onto the object.

Take a look at the working example above where you retrieved the list. Notice that the keys in your `Issue` type are in that log, but are missing here. The assignment has failed, and all of the `Issue` properties are `null`.

---

## Conclusion

In this guide, you've learned how to use the `useReadContract` hook to call `pure` and `view` functions from your smart contracts. You then converted this data into React state and displayed it to the user. Finally, you explored a tricky edge case in which the presence of a nested `mapping` can cause a confusing bug when using the automatically-generated getter.

---

## Simple DAO Contract Example

Use this contract if you don't have your own from the [ERC 20 Tokens Exercise]. You can also use this if you want to cheat to get that badge. Doing so would be silly though!

:::caution
If you use your own contract, redeploy it with the `numberOfIssues` and `getAllIssues` functions from the bottom of the contract below. We'll need this for our first pass solution for getting all the `Issues` in the contract.

**You also need to make the `getIssue` function `public`. The original spec called for it to be `external`.**
:::

```Solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract FEWeightedVoting is ERC20 {
    using EnumerableSet for EnumerableSet.AddressSet;

    mapping(address => bool) claimed;
    uint public maxSupply = 1000000;
    uint totalClaimed;

    uint constant claimAmount = 100;

    error TokensClaimed();
    error AllTokensClaimed();
    error NoTokensHeld();
    error QuorumTooHigh(uint);
    error AlreadyVoted();
    error VotingClosed();

    enum Vote {
        AGAINST,
        FOR,
        ABSTAIN
    }

    struct Issue {
        EnumerableSet.AddressSet voters;
        string issueDesc;
        uint votesFor;
        uint votesAgainst;
        uint votesAbstain;
        uint totalVotes;
        uint quorum;
        bool passed;
        bool closed;
    }

    // EnumerableSets are mappings and cannot be returned outside a contract
    struct ReturnableIssue {
        address[] voters;
        string issueDesc;
        uint votesFor;
        uint votesAgainst;
        uint votesAbstain;
        uint totalVotes;
        uint quorum;
        bool passed;
        bool closed;
    }

    Issue[] issues;

    constructor(
        string memory _name,
        string memory _symbol
    ) ERC20(_name, _symbol) {
        // Burn Issue 0
        issues.push();
    }

    function claim() public {
        if (claimed[msg.sender] == true) {
            revert TokensClaimed();
        }

        if (totalSupply() >= maxSupply) {
            revert AllTokensClaimed();
        }

        _mint(msg.sender, claimAmount);
        claimed[msg.sender] = true;
    }

    function createIssue(
        string memory _issueDesc,
        uint _quorum
    ) public returns (uint) {
        if (balanceOf(msg.sender) == 0) {
            revert NoTokensHeld();
        }

        if (_quorum > totalSupply()) {
            revert QuorumTooHigh(_quorum);
        }

        Issue storage newIssue = issues.push();
        newIssue.issueDesc = _issueDesc;
        newIssue.quorum = _quorum;
        return issues.length - 1;
    }

    function getIssue(uint _id) public view returns (ReturnableIssue memory) {
        Issue storage issue = issues[_id];
        return
            ReturnableIssue(
                issue.voters.values(),
                issue.issueDesc,
                issue.votesFor,
                issue.votesAgainst,
                issue.votesAbstain,
                issue.totalVotes,
                issue.quorum,
                issue.closed,
                issue.passed
            );
    }

    function vote(uint _issueId, Vote _vote) public {
        Issue storage issue = issues[_issueId];
        if (issue.voters.contains(msg.sender)) {
            revert AlreadyVoted();
        }
        if (issue.closed) {
            revert VotingClosed();
        }
        issue.voters.add(msg.sender);

        if (_vote == Vote.FOR) {
            issue.votesFor += balanceOf(msg.sender);
        } else if (_vote == Vote.AGAINST) {
            issue.votesAgainst += balanceOf(msg.sender);
        } else if (_vote == Vote.ABSTAIN) {
            issue.votesAbstain += balanceOf(msg.sender);
        } else {
            revert("Error...");
        }

        issue.totalVotes += balanceOf(msg.sender);

        if (issue.totalVotes >= issue.quorum) {
            issue.closed = true;
            if (issue.votesFor > issue.votesAgainst) {
                issue.passed = true;
            }
        }
    }

    function numberOfIssues() public view returns(uint) {
        return issues.length;
    }

    function getAllIssues() public view returns(ReturnableIssue[] memory) {
        ReturnableIssue[] memory allIssues = new ReturnableIssue[](issues.length);

        for(uint i = 0; i < issues.length; i++) {
            allIssues[i] = getIssue(i);
        }

        return allIssues;
    }
}
```

---

[RainbowKit]: https://www.rainbowkit.com/
[wagmi]: https://wagmi.sh/
[quick start]: https://www.rainbowkit.com/docs/installation/
[Wallet Connectors]: ../frontend-setup/wallet-connectors/
[`useAccount`]: https://wagmi.sh/react/hooks/useAccount
[hydration error]: https://nextjs.org/docs/messages/react-hydration-error
[ERC 20 Tokens Exercise]: https://docs.base.org/base-learn/docs/erc-20-token/erc-20-exercise
[Sepolia BaseScan]: https://sepolia.basescan.org/
[`useAccount` hook]: ./useAccount
[Hardhat]: https://hardhat.org/
[ABI]: https://docs.soliditylang.org/en/latest/abi-spec.html
[`useReadContract`]: https://wagmi.sh/react/hooks/useReadContract



<!-- File: ../web/apps/base-docs/base-learn/docs/reading-and-displaying-data/configuring-useReadContract.md -->

---
title: Configuring `useReadContract`
description: Configure the properties of the `useReadContract` hook.
hide_table_of_contents: false
---

The [`useReadContract`] hook has a number of configurable properties that will allow you to adapt it to your needs. You can combine the functionality of TanStack queries with [`useBlockNumber`] to watch the blockchain for changes, although doing so will consume a number of API calls.

---

## Objectives

By the end of this guide you should be able to:

- Use `useBlockNumber` and the `queryClient` to automatically fetch updates from the blockchain
- Describe the costs of using the above, and methods to reduce those costs
- Configure arguments to be passed with a call to a `pure` or `view` smart contract function
- Call an instance of `useReadContract` on demand
- Utilize `isLoading` and `isFetching` to improve user experience

---

## Fetching Updates from the Blockchain

You'll continue with the project you've been building and last updated while learning about the [`useReadContract` hook].

Once the excitement of your accomplishment of finally reading from your own contract subsides, try using BaseScan to add another issue, or vote on an existing issue. You'll notice that your frontend does **not** update. There are a few ways to handle this.

### The Watch Feature

The easiest is to use `useBlockNumber` with the `watch` feature to automatically keep track of the block number, then use the `queryClient` to update when that changes. **Make sure** you decompose the `queryKey` from the return of `useReadContract`.

```tsx
import { useEffect, useState } from 'react';
import { useReadContract, useBlockNumber } from 'wagmi';
import { useQueryClient } from '@tanstack/react-query';

// Other Code

export function IssueList() {
  // Other Code

  const queryClient = useQueryClient();
  const { data: blockNumber } = useBlockNumber({ watch: true });

  const {
    data: issuesData,
    isError: issuesIsError,
    isPending: issuesIsPending,
    queryKey: issuesQueryKey,
  } = useReadContract({
    address: contractData.address as `0x${string}`,
    abi: contractData.abi,
    functionName: 'getAllIssues',
  });

  // Note that this is a separate `useEffect` from the one that handles the
  // update after the list of issues is returned
  useEffect(() => {
    queryClient.invalidateQueries({ queryKey: issuesQueryKey });
  }, [blockNumber, queryClient, issuesQueryKey]);

  // Return code
}
```

Try adding a new issue and it will automatically appear on the list, although it may take more time than you are used to. Blockchain is still slower than the web.

It works! Unfortunately, you can't really stop here, unless you're working on a hackathon prototype or a very early stage demo. The catch is that `wagmi` has a default [`pollingInterval`] of 4 seconds, so having this `watch` causes it to call `eth_blocknumber` constantly, which then triggers an `eth_call`, both of which use api credits.

If you were to take the obvious approach of adding a `useReadContract` for every function you wanted data from, and set it to `watch`, things would quickly get out of hand. A single open web page with 15 functions watched in this way will hit rate-limiting in as short as an hour.

:::info

Don't do this, either use multi-call via [`useReadContracts`], or consolidate your `view`s into a single function that fetches all the data you need in one call.

:::

Luckily, you have options to control these calls a little better.

### Pausing On Blur

Once quick improvement is to simply stop watching the blockchain if the website doesn't have focus. To see this in action, add a state variable to count how many times the function has settled, and one for if the page is focused. You'll also need to set up event listeners to set the state of the latter when the page is focused or blurred.

```tsx
const [timesCalled, setTimesCalled] = useState(0);
const [pageIsFocused, setPageIsFocused] = useState(true);

useEffect(() => {
  const onFocus = () => setPageIsFocused(true);
  const onBlur = () => setPageIsFocused(false);

  window.addEventListener('focus', onFocus);
  window.addEventListener('blur', onBlur);

  return () => {
    window.removeEventListener('focus', onFocus);
    window.removeEventListener('blur', onBlur);
  };
}, []);
```

Then, update the `watch` for `useBlockNumber` so that it only does so if `pageIsFocused`.

```tsx
const { data: blockNumber } = useBlockNumber({ watch: pageIsFocused });
```

Add a line to the `useEffect` for `blockNumber` increment your counter as well.

```tsx
useEffect(() => {
  setTimesCalled((prev) => prev + 1);
  queryClient.invalidateQueries({ queryKey: issuesQueryKey });
}, [blockNumber, queryClient]);
```

Finally, surface your counter in the component.

```tsx
return (
  <div>
    <h2>Number of times called</h2>
    <p>{timesCalled.toString()}</p>
    <p>{'Has focus: ' + pageIsFocused}</p>
    <h2>All Issues</h2>
    <div>{renderIssues()}</div>
  </div>
);
```

Now, when you watch the page, the count will go up every four seconds. When you switch to another tab or window, the counter will pause until you switch back.

### Adjusting the Polling Rate

You likely need to share timely updates with your users, but how timely do those updates need to be to meet the requirements of your app? If you're doing instant messaging, 4 seconds may even be too long (though any faster is running into the speed blocks are added in most L2s).

A more robust DAO is going to have a voting period of at least a day or two, so those users probably don't need to see that there is a new issue within 4 seconds of it hitting the chain.

Adjust your [`pollingInterval`] by setting it in `getDefaultConfig` in `_app.tsx`:

```tsx
const config = getDefaultConfig({
  appName: 'RainbowKit App',
  projectId: 'YOUR_PROJECT_ID',
  chains: [baseSepolia],
  ssr: true,
  pollingInterval: 30_000,
});
```

Setting it to 30 seconds, or 30,000 milliseconds, will reduce your API calls dramatically, without negatively impacting members of the DAO.

You can also set `pollingInterval` if you're using `createConfig` instead of the default.

### Updating on Demand

You can use a similar system to call your update function on demand. First, add a button, a handler for that button, and a state variable for it to set:

```tsx
const [triggerRead, setTriggerRead] = useState(false);

const handleTriggerRead = () => {
  setTriggerRead(true);
};
```

```tsx
return (
  <div>
    <button onClick={handleTriggerRead}>Read Now</button>
    <h2>Number of times called</h2>
    <p>{timesCalled.toString()}</p>
    <p>{'Has focus: ' + pageIsFocused}</p>
    <h2>All Issues</h2>
    <div>{renderIssues()}</div>
  </div>
);
```

Finally, set `watch` to equal `triggerRead`, instead of `pageIsFocused`, and reset `triggerRead` in the `useEffect`.

```tsx
const { data: blockNumber } = useBlockNumber({ watch: triggerRead });

// Other code...

useEffect(() => {
  setTriggerRead(false);
  queryClient.invalidateQueries({ queryKey: issuesQueryKey });
}, [blockNumber, queryClient]);
```

Now, when the user clicks the button, the hook will call the read function a single time, then set `watch` back to false.

---

## Setting UI Elements

You can use the "is" return values to set UI elements depending on the status of the hook as it attempts to call a function on the blockchain.

Try to modify your button to provide feedback to the user that the function has been called.

```tsx
// Bad code example, do not use
<button disabled={issuesIsLoading} onClick={handleTriggerRead}>
  {issuesIsLoading ? 'Loading' : 'Read Now'}
</button>
```

The above code won't break anything, but nothing will appear to happen. This happens because `isLoading` is only `true` in circumstances where data is loading for the first time, but no data is present. You could use this to show a spinning wheel in place of the list of issues.

Instead, try decomposing `isFetching` in your `useReadContract`. This property is true while data is being fetched, even if data has already been loaded once.

```tsx
// Imperfect code example, do not use
<button disabled={issuesIsFetching} onClick={handleTriggerRead}>
  {issuesIsFetching ? 'Loading' : 'Read Now'}
</button>
```

You'll probably see the button flicker very quickly since the call doesn't take very long. For a production app, you'd need to add additional handling to smooth out the experience.

---

## Passing Arguments

Arguments are passed into a `useReadContract` hook by adding an array of arguments, in order, to the `args` property. Common practice is to use React state variables set by UI elements to enable the arguments to be set and modified. For example, you might create a drop-down to set `issueNumber`, then fetch that issue with:

```tsx
// Incomplete code stub
const [issueNumber, setIssueNumber] = useState(0);

const { isLoading: getIssueIsLoading } = useReadContract({
  address: contractData.address as `0x${string}`,
  abi: contractData.abi,
  functionName: 'getIssue',
  args: [issueNumber],
});
```

Depending on your design needs, you can use the techniques above to either watch constantly for updates, or fetch them on user action.

---

## Conclusion

In this guide, you've learned how to use the `watch` feature of `useBlockNumber` combined with `useEffect` and `queryClient.invalidateQueries` to enable your frontend to see updates to your smart contract. You've also learned the costs of doing so, and some strategies for mitigation. You've learned how to pass arguments to your functions. Finally, you've learned how to use the properties returned by `useReadContract` to adjust your UI to improve the experience for your users.

---

[wagmi]: https://wagmi.sh/
[`useReadContract`]: https://wagmi.sh/react/hooks/useReadContract
[`useReadContract` hook]: ./useReadContract
[`useBlocNumber`]: https://wagmi.sh/react/api/hooks/useBlockNumber
[removed]: https://wagmi.sh/react/guides/migrate-from-v1-to-v2#removed-watch-property
[`useReadContracts`]: https://wagmi.sh/react/hooks/useReadContracts
[`pollingInterval`]: https://wagmi.sh/react/api/createConfig#pollinginterval



<!-- File: ../web/apps/base-docs/base-learn/docs/development-tools/overview.md -->

---
title: Overview
description: Learn about development environment options
keywords:
  [Hardhat, Foundry, Remix, smart contract development, development, development environments]
hide_table_of_contents: false
---

As the popularity and possibilities of building onchain have increased, so has the number, quality, and ease of setup for a variety of smart contract development environments. Most of the smart contract development content in Base Learn is done in [Remix], an online IDE that allows you to dive right into learning without worrying about setup.

However, the setup of professional tools for local development is far less burdensome than it used to be. [Foundry] and [Hardhat] are two popular choices, both with excellent communities.

You may wish to select and install one of these now, but feel free to skip those sections and go to right [Smart Contract Development] if you're happy learning with an online editor!

[Remix]: https://remix.ethereum.org/
[Foundry]: https://book.getfoundry.sh/
[Hardhat]: https://hardhat.org/
[Smart Contract Development]: ../introduction-to-solidity/introduction-to-solidity-overview



<!-- File: ../web/apps/base-docs/base-learn/docs/advanced-functions/function-modifiers.md -->

---
title: Function Modifiers
description: Build custom function modifiers to efficiently modify functionality.
hide_table_of_contents: false
---

Function modifiers allow you to efficiently change the behavior of functions. In some ways, it's similar to inheritance, but there are restrictions, particularly in variable scope.

---

## Objectives

By the end of this lesson you should be able to:

- Use modifiers to efficiently add functionality to multiple functions

---

## Adding a Simple OnlyOwner Modifier

By default, `public` functions can be called by **anyone**, without restriction. Often this is desirable. You want any user to be able to see what NFTs are for sale on your platform, sign up for a service, or read various items stored in state.

However, there will be many functions you **don't** want any user to be able to do, such as setting the fee for using the app, or withdrawing all funds in the contract! A common pattern to protect these functions is to use `modifier`s to make sure that only the owner can call these functions.

:::caution

For a production app, you'll want to use a more robust implementation of `onlyOwner`, such as the [one provided by OpenZeppelin].

:::

### Adding an Owner

The address of the deployer of a contract is **not** included as an accessible property. To make it available, add it as a state variable and assign `msg.sender` in the `constructor`.

<details>

<summary>Reveal code</summary>

```solidity
contract Modifiers {
    address owner;

    constructor () {
        owner = msg.sender;
    }
}
```

</details>

<br />

### Creating an `onlyOwner` Modifier

[Modifiers] are very similar to functions and are declared with the `modifier` keyword. The modifier can run any Solidity code, including functions, and is allowed to modify state. Modifiers must have a special `_` character, which serves as a placeholder for where the code contained within the modified function will run.

Create a simple `onlyOwner` modifier, which returns an `error` of `NotOwner` with the sending address if the sender is not the owner.

<details>

<summary>Reveal code</summary>

```solidity
error NotOwner(address _msgSender);
```

```solidity
modifier onlyOwner {
    if (msg.sender != owner) {
        revert NotOwner(msg.sender);
    }
    _;
}
```

</details>

<br/>

Test your `modifier` by adding a function that uses it:

<details>

<summary>Reveal code</summary>

```solidity
function iOwnThis() public view onlyOwner returns (string memory) {
    return "You own this!";
}
```

</details>

<br/>

To test, deploy your contract and call the `iOwnThis` function. You should see the message "You own this!".

Next, switch the _Account_, and try the function again. You should see an error in the console:

```text
call to Modifiers.iOwnThis errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Error provided by the contract:
NotOwner
Parameters:
{
 "_msgSender": {
  "value": "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db"
 }
}
Debug the transaction to get more information.
```

:::caution

Always verify the output of a function call in the console. The result that appears under the button for the function is convenient, but it does **not** clear or change if a subsequent call reverts.

:::

---

## Modifiers and Variables

Modifiers can have parameters, which essentially work the same as in functions. These parameters can be independent values, or they can overlap with the arguments provided to a function call.

### Modifiers with Parameters

Modifier parameters can be the arguments provided to the functions they modify. You can perform calculations and trigger errors based on these values.

```solidity
error NotEven(uint number);

modifier onlyEven(uint _number) {
    if(_number % 2 != 0) {
        revert NotEven(_number);
    }
    _;
}

function halver(uint _number) public pure onlyEven(_number) returns (uint) {
    return _number / 2;
}
```

### Independent Scope

While `modifiers` are used to modify functions and can share inputs, they have separate scopes. The following example will **not** work:

```solidity
// Bad code example, does not work
modifier doubler(uint _number) {
    _number *= 2;
    _;
}

function modifierDoubler(uint _number) public pure doubler(_number) returns (uint) {
    return _number; // Returns the original number, NOT number * 2
}
```

---

## Conclusion

Function `modifier`s are an efficient and reusable way to add checks, trigger errors, and control function execution. In this lesson, you've seen examples of how they can be used to abort execution under certain conditions. You've also learned that they have separate scopes and cannot be used to modify variables within the function they modify.

[one provided by OpenZeppelin]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol



<!-- File: ../web/apps/base-docs/base-learn/docs/advanced-functions/function-visibility-vid.md -->

---
title: Function Visibility
description: Learn how to control the visibility of functions.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804676890' title='Function Visibility' />



<!-- File: ../web/apps/base-docs/base-learn/docs/advanced-functions/function-visibility.md -->

---
title: Function Visibility and State Mutability
description: A quick reference for all your function declaring needs.
hide_table_of_contents: false
---

You've seen much of this before, but this document outlines and highlights the options for _function visibility_ and _state mutability_ all in one document.

---

## Objectives

By the end of this lesson you should be able to:

- Categorize functions as public, private, internal, or external based on their usage
- Describe how pure and view functions are different than functions that modify storage

---

## Function Visibility

There are four types of [visibility] for functions in Solidity: `external`, `public`, `internal`, and `private`. These labels represent a further division of the _public_ and _private_ labels you might use in another language.

### External

Functions with `external` visibility are **only** callable from other contracts and cannot be called within their own contract. You may see older references stating you should use `external` over `public` because it forces the function to use `calldata`. This is no longer correct, because both function visibilities can now use `calldata` and `memory` for parameters. However, using `calldata` for either will cost less gas.

```solidity
contract Foo {
    constructor() {
        // Bad code example, will not work
        uint bar = foo(3);
        // ... other code
    }

    function foo(uint _number) external pure returns (uint) {
         return _number*2;
    }
}
```

### Public

Public functions work the same as external, except they may also be called within the contract that contains them.

```solidity
contract Foo {
    constructor() {
        // Public functions may be called within the contract
        uint bar = foo(3);
        // ... other code
    }

    function foo(uint _number) public pure returns (uint) {
        return _number*2;
    }
}
```

### Private and Internal

Functions visible as `private` and `internal` operate nearly identically. Beyond writing hygienic code, these have a very important effect. Because they are not a part of the contract's ABI, you can use `mapping`s and `storage` variable references as parameters.

The difference is that `private` functions can't be called from derived contracts. You'll learn more about that when we cover inheritance.

Some developers prepend an underscore to `private` and `internal` functions.

```solidity
function _foo(uint _number) private returns (uint) {
    return _number*2;
}
```

:::warning

All data on a blockchain is public. Don't mistake hiding visibility while coding for hiding information from the world!

:::

---

## Function State Mutability

State mutability labels are relatively unique to Solidity. They determine how a function can interact with state, which has a substantial impact on gas costs.

### Pure

`pure` functions promise to neither read nor write state. They're usually used for helper functions that support other functionality.

```solidity
function abs(int x) public pure returns (int) {
    return x >= 0 ? x : -x;
}
```

`pure` functions can be called from outside the blockchain without using gas, if they are also `public` or `external`.

### View

`view` functions access state, but don't modify it. You've used these for tasks such as returning all the values in an array.

```solidity
function getArr() public view returns (uint[] memory) {
    return arr;
}
```

`view` functions can be called from outside the blockchain without using gas, if they are also `public` or `external`.

### Unlabeled Functions

Functions that are not labeled `view` or `pure` can modify state and the compiler will generate a warning if they do not.

```solidity
function addToArr(uint _number) public {
    arr.push(_number);
}
```

They can have any visibility and will always cost gas when called.

---

## Conclusion

The visibility and mutability keywords in Solidity help you organize your code and alert other developers to the properties of each of your functions. Use them to keep your code organized and readable.

---

[visibility]: https://docs.soliditylang.org/en/v0.8.17/contracts.html?highlight=pure#function-visibility



<!-- File: ../web/apps/base-docs/base-learn/docs/advanced-functions/function-modifiers-vid.md -->

---
title: Function Modifiers
description: Use modifiers to control how functions work.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804676855' title='Function Modifiers' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-tools-and-testing/overview.md -->

---
title: 'Overview'
slug: /hardhat-tools-and-testing/overview
description: What's in this learning material.
author: Brian Doyle
keywords:
  [
    Hardhat Tools,
    Smart Contract Development,
    Gas Optimization,
    Debugging,
    Test Coverage,
    Contract Size,
    Solidity,
    Base network,
    Base blockchain,
    blockchain development,
  ]
hide_table_of_contents: false
displayed_sidebar: null
---

# Overview of Hardhat Tools and Testing

This series of guides shows you how to use a number of [Hardhat plugins] that will help you more effectively build and test your smart contracts.

Learn how to keep your contracts under the 24 kiB limit, improve gas costs for your users, make sure your unit tests fully cover your code, and practice debugging.

---

## Objectives

By the end of these guides, you should be able to:

### Profiling Size

- Use Hardhat Contract Sizer plugin to profile contract size
- Describe common strategies for managing the contract size limit
- Describe the impact that inheritance has on the byte code size limit
- Describe the impact that external contracts have on the byte code size limit
- Describe the impact of using libraries has on the byte code size limit
- Describe the impact of using the Solidity optimizer

### Profiling Gas

- Use the Hardhat Gas Reporter plugin to profile gas usage
- Describe common strategies for improving the gas usage of a contract

### Debugging

- Use `console.log` to write debugging logs
- List common errors and their resolutions
- Determine if an error is a contract error or an error in the test

### Test Coverage

- Use the Solidity Coverage plugin to analyze the coverage of your test suite
- Increase the coverage of your test suite

---

## Prerequisites

### 1. Basic understanding of writing smart contracts

These guides assume that you're reasonably comfortable writing basic smart contracts. If you're just getting started, jump over to our [Base Learn] guides and start learning!

### 2. Familiarity with Hardhat

We also assume that you've got Hardhat up and running, and can write unit tests for your smart contracts. If you're not there yet, but already know Solidity, you can [setup Hardhat here].

[setup Hardhat here]: https://docs.base.org/base-learn/docs/hardhat-setup-overview/hardhat-setup-overview-sbs
[Hardhat plugins]: https://hardhat.org/hardhat-runner/plugins
[Base Learn]: https://base.org/learn



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/inheritance-exercise.md -->

---
title: Inheritance Exercise
description: Exercise - Demonstrate your knowledge of inheritance.
hide_table_of_contents: false
---

Create contracts that adhere to the following specifications.

---

## Contracts

### Employee

Create an `abstract` contract called `Employee`. It should have:

- A public variable storing `idNumber`
- A public variable storing `managerId`
- A constructor that accepts arguments for and sets both of these variables
- A `virtual` function called `getAnnualCost` that returns a `uint`

### Salaried

A contract called `Salaried`. It should:

- Inherit from `Employee`
- Have a public variable for `annualSalary`
- Implement an `override` function for `getAnnualCost` that returns `annualSalary`
- An appropriate constructor that performs any setup, including setting `annualSalary`

### Hourly

Implement a contract called `Hourly`. It should:

- Inherit from `Employee`
- Have a public variable storing `hourlyRate`
- Include any other necessary setup and implementation

:::tip

The annual cost of an hourly employee is their hourly rate \* 2080 hours.

:::

### Manager

Implement a contract called `Manager`. It should:

- Have a public array storing employee Ids
- Include a function called `addReport` that can add id numbers to that array
- Include a function called `resetReports` that can reset that array to empty

### Salesperson

Implement a contract called `Salesperson` that inherits from `Hourly`.

### Engineering Manager

Implement a contract called `EngineeringManager` that inherits from `Salaried` and `Manager`.

## Deployments

You'll have to do a more complicated set of deployments for this exercise.

Deploy your `Salesperson` and `EngineeringManager` contracts. You don't need to separately deploy the other contracts.

Use the following values:

### Salesperson

- Hourly rate is 20 dollars an hour
- Id number is 55555
- Manager Id number is 12345

### Manager

- Annual salary is 200,000
- Id number is 54321
- Manager Id is 11111

## Inheritance Submission

Copy the below contract and deploy it using the addresses of your `Salesperson` and `EngineeringManager` contracts.

```solidity
contract InheritanceSubmission {
    address public salesPerson;
    address public engineeringManager;

    constructor(address _salesPerson, address _engineeringManager) {
        salesPerson = _salesPerson;
        engineeringManager = _engineeringManager;
    }
}
```

---

## Submit your Contracts and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

:::caution

Submit your address for your copy of the `InheritanceSubmission` contract that contains your other contract addresses.

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={8}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/multiple-inheritance.md -->

---
title: Multiple Inheritance
description: Learn how to have a contract inherit from multiple contracts.
hide_table_of_contents: false
---

Contracts can inherit from more than one contract. In this lesson, we'll explore how multiple inheritance works in Solidity.

---

## Objectives

By the end of this lesson you should be able to:

- Write a smart contract that inherits from multiple contracts

---

## Multiple Inheritance

Continue working with your contracts in `Inheritance.sol`. Add a new contract called `ContractC` with another `whoAmI` function:

<details>

<summary>Reveal code</summary>

```solidity
contract ContractC {
    function whoAmI() external pure returns (string memory) {
        return "contract C";
    }
}
```

</details>

<br/>

### Inheriting from Two Contracts

You can inherit from additional contracts by simply adding a comma and that contract's name after the first. Add inheritance from `ContractC` (an error is expected):

<details>

<summary>Reveal code</summary>

```solidity
// bad code example, do not use
contract ContractA is ContractB, ContractC {
    function whoAmExternal() external pure returns (string memory) {
        return whoAmIInternal();
    }
}
```

</details>

<br/>

The error is because both `ContractB` and `ContractC` contain a function called `whoAmI`. As a result, the compiler needs instruction on which to use.

```text
from solidity:
TypeError: Derived contract must override function "whoAmI". Two or more base classes define function with same name and parameter types.
  --> contracts/Inheritance.sol:21:1:
   |
21 | contract ContractA is ContractB, ContractC {
   | ^ (Relevant source part starts here and spans across multiple lines).
Note: Definition in "ContractC":
 --> contracts/Inheritance.sol:6:5:
  |
6 |     function whoAmI() external pure returns (string memory) {
  |     ^ (Relevant source part starts here and spans across multiple lines).
Note: Definition in "ContractB":
  --> contracts/Inheritance.sol:12:5:
   |
12 |     function whoAmI() external pure returns (string memory) {
   |     ^ (Relevant source part starts here and spans across multiple lines).
```

### Using Virtual and Override

One method to resolve this conflict is to use the [`virtual` and `override`] keywords to enable you to add functionality to choose which to call.

Add the `virtual` keyword to the `whoAmI` function in both `ContractC` and `ContractB`.

They must also be made `public` instead of `external`, because `external` functions cannot be called within the contract.

```solidity
contract ContractC {
    function whoAmI() public virtual pure returns (string memory) {
        return "contract C";
    }
}

contract ContractB {
    function whoAmI() public virtual pure returns (string memory) {
        return "contract B";
    }

    // ... additional code
}
```

Add an `override` function called `whoAmI` to `ContractA`:

```solidity
// Bad code example, do not use
function whoAmI() public override pure returns (string memory) {
    return ContractB.whoAmI();
}
```

You'll get another error, telling you to specify which contracts this function should override.

```text
from solidity:
TypeError: Function needs to specify overridden contracts "ContractB" and "ContractC".
  --> contracts/Inheritance.sol:22:32:
   |
22 |     function whoAmI() public override pure returns (string memory) {
   |                              ^^^^^^^^
```

Add them both:

```solidity
function whoAmI() external override(ContractB, ContractC) pure returns (string memory) {
    return ContractB.whoAmI();
}
```

Deploy and test. The call will now be back to reporting "contract B".

### Changing Types Dynamically

Add an `enum` at the contract level in `ContractA` with members for `None`, `ContractBType`, and `ContractCType`, and an instance of it called `contractType`.

<details>

<summary>Reveal code</summary>

```solidity
enum Type { None, ContractBType, ContractCType }

Type contractType;
```

</details>

<br/>

Add a `constructor` to `ContractA` that accepts a `Type` and sets `initialType`.

<details>

<summary>Reveal code</summary>

```solidity
constructor (Type _initialType) {
    contractType = _initialType;
}
```

</details>

<br/>

Update `whoAmI` in `ContractA` to call the appropriate `virtual` function based on its `currentType`.

<details>

<summary>Reveal code</summary>

```solidity
// Bad code example, do not use
function whoAmI() public override(ContractB, ContractC) pure returns (string memory) {
    if(contractType == Type.ContractBType) {
        return ContractB.whoAmI();
    }
    if(contractType == Type.ContractCType) {
        return ContractC.whoAmI();
    }
    return "contract A";
}
```

</details>

<br/>

You'll get errors because the function now reads from state, so it is no longer `pure`. Update it to `view`. You'll also have to update the `whoAmI` `virtual` functions to `view` to match.

<details>

<summary>Reveal code</summary>

```solidity
function whoAmI() public override(ContractB, ContractC) view returns (string memory) {
    if(contractType == Type.ContractBType) {
        return ContractB.whoAmI();
    }
    if(contractType == Type.ContractCType) {
        return ContractC.whoAmI();
    }
    return "contract A";
}
```

</details>

<br/>

Finally, add a function that allows you to switch `currentType`:

<details>

<summary>Reveal code</summary>

```solidity
function changeType(Type _newType) external {
    contractType = _newType;
}
```

</details>

<br/>

Deploy and test. You'll need to use **0**, **1**, and **2** as values to set `contractType`, because Remix won't know about your `enum`.

## Final Code

After completing this exercise, you should have something similar to:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract ContractC {
    function whoAmI() public virtual view returns (string memory) {
        return "contract C";
    }
}

contract ContractB {
    function whoAmI() public virtual view returns (string memory) {
        return "contract B";
    }

    function whoAmIInternal() internal pure returns (string memory) {
        return "contract B";
    }
}

contract ContractA is ContractB, ContractC {
    enum Type { None, ContractBType, ContractCType }

    Type contractType;

    constructor (Type _initialType) {
        contractType = _initialType;
    }

    function changeType(Type _newType) external {
        contractType = _newType;
    }

    function whoAmI() public override(ContractB, ContractC) view returns (string memory) {
        if(contractType == Type.ContractBType) {
            return ContractB.whoAmI();
        }
        if(contractType == Type.ContractCType) {
            return ContractC.whoAmI();
        }
        return "contract A";
    }

    function whoAmExternal() external pure returns (string memory) {
        return whoAmIInternal();
    }
}
```

---

## Conclusion

In this lesson, you've explored how to use multiple inheritance to import additional functionality into a contract. You've also implemented one approach to resolving name conflicts between those contracts.

---

[`virtual` and `override`]: https://docs.soliditylang.org/en/v0.8.17/contracts.html?#function-overriding



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/abstract-contracts-vid.md -->

---
title: Abstract Contracts
description: Create contracts that exist only to be inherited from.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035946' title='Abstract Contracts' />



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/abstract-contracts-sbs.md -->

---
title: Abstract Contracts
description: Learn how to make contracts that must be inherited by another contract.
hide_table_of_contents: false
---

[Abstract] contracts can't exist on their own. Their functionality can only be utilized by a contract that inherits from them. In this lesson, you'll learn how to create an abstract contract.

---

## Objectives

By the end of this lesson you should be able to:

- Use the virtual, override, and abstract keywords to create and use an abstract contract

---

## Abstract Contracts

Continue with your `Inheritance.sol` file. Add `ContractD` as an `abstract contract`. Add a `virtual` function called `whoAreYou` function, but do **not** add any implementation for that function.

<details>

<summary>Reveal code</summary>

```solidity
abstract contract ContractD {
    function whoAreYou() public virtual view returns (string memory);
}
```

</details>

<br/>

### Inheriting from an Abstract Function

Update `ContractA` to inherit from `ContractD`.

You'll get a slightly confusing error that `ContractA` needs to be marked as `abstract`. Doing so is **not** the correct fix.

```text
from solidity:
TypeError: Contract "ContractA" should be marked as abstract.
  --> contracts/Inheritance.sol:25:1:
   |
25 | contract ContractA is ContractB, ContractC, ContractD {
   | ^ (Relevant source part starts here and spans across multiple lines).
Note: Missing implementation:
 --> contracts/Inheritance.sol:6:5:
  |
6 |     function whoAreYou() public virtual view returns (string memory);
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

The clue for the correct solution is further down: `Note:  Missing implementation:`

Only `abstract` contracts can declare functions that are not implemented. To fix this, provide an `override` implementation for `whoAreYou` in `ContractA`:

<details>

<summary>Reveal code</summary>

```solidity
function whoAreYou() public override pure returns (string memory) {
    return "I'm a person!";
}
```

</details>


---

## Conclusion

In this lesson, you've learned how to implement and inherit from an abstract contract.

---

[Abstract]: https://docs.soliditylang.org/en/v0.8.17/contracts.html?#abstract-contracts



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/multiple-inheritance-vid.md -->

---
title: Multiple Inheritance
description: Create contracts that inherit from multiple contracts.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035992' title='Multiple Inheritance' />



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/inheritance-vid.md -->

---
title: Inheritance
description: Create contracts that inherit from other contracts.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035971' title='Inheritance' />



<!-- File: ../web/apps/base-docs/base-learn/docs/inheritance/inheritance-sbs.md -->

---
title: Inheritance
description: Learn how to use inheritance to bring functionality from one contract into another.
hide_table_of_contents: false
---

Solidity is an object-oriented language. Contracts can inherit from one another, allowing efficient reuse of code.

---

## Objectives

By the end of this lesson you should be able to:

- Write a smart contract that inherits from another contract
- Describe the impact inheritance has on the byte code size limit

---

## Inheritance

Create a new contract file in Remix called `Inheritance.sol` and add two simple contracts, each with a function identifying which contract called it:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract ContractB {
    function whoAmI() external pure returns (string memory) {
        return "contract B";
    }
}

contract ContractA {
    function whoAmI() external pure returns (string memory) {
        return "contract A";
    }
}
```

`ContractA` says that it is "contract A" and `ContractB` says that it is "contract B".

### Inheriting from Another Contract

[Inheritance] between contracts is indicated by the `is` keyword in the contract declaration. Update `ContractA` so that it `is` `ContractB`, and delete the `whoAmI` function from `ContractA`.

<details>

<summary>Reveal code</summary>

```solidity
contract ContractB {
    function whoAmI() external pure returns (string memory) {
        return "contract B";
    }
}

contract ContractA is ContractB {

}
```

</details>

<br/>

Deploy and test again. Even though `ContractA` doesn't have any functions in it, the deployment still shows the button to call `whoAmI`. Call it. `ContractA` now reports that it is "contract B", due to the inheritance of the function from `Contract B`.

### Internal Functions and Inheritance

Contracts can call the `internal` functions from contracts they inherit from. Add an `internal` function to `ContractB` called `whoAmIInternal` that returns "contract B".

Add an external function called `whoAmIExternal` that returns the results of a call to `whoAmIInternal`.

<details>

<summary>Reveal code</summary>

```solidity
contract ContractB {
    function whoAmI() external pure returns (string memory) {
        return "contract B";
    }

    function whoAmIInternal() internal pure returns (string memory) {
        return "contract B";
    }
}

contract ContractA is ContractB {
    function whoAmExternal() external pure returns (string memory) {
        return whoAmIInternal();
    }
}
```

</details>

<br/>

Deploy and test. Note that in the deployment for `ContractB`, the `whoAmIInternal` function is **not** available, as it is `internal`. However, calling `whoAmIExternal` can call the `internal` function and return the expected result of "contract B".

### Internal vs. Private

You cannot call a `private` function from a contract that inherits from the contract containing that function.

```solidity
// Bad code example, do not use
contract ContractB {
    function whoAmIPrivate() private pure returns (string memory) {
        return "contract B";
    }
}

contract ContractA is ContractB {
    function whoAmExternal() external pure returns (string memory) {
        return whoAmIPrivate();
    }
}
```

The compiler will raise an error:

```text
from solidity:
DeclarationError: Undeclared identifier.
  --> contracts/Inheritance.sol:17:16:
   |
17 |         return whoAmIPrivate();
   |                ^^^^^^^^^^^^^
```

### Inheritance and Contract Size

A contract that inherits from another contract will have that contract's bytecode included within its own. You can view this by opening settings in Remix and turning _Artifact Generation_ back on. The bytecode for each compiled contract will be present in the JSON file matching that contract's name within the `artifacts` folder.

Any empty contract:

```solidity
contract EmptyContract {

}
```

Will compile into something similar to this:

```text
6080604052600080fdfea2646970667358221220df894b82f904e22617d7e40150306e2d2e8cb2ca5dcacb666a0c3d40f5f988c464736f6c63430008110033
```

A slightly more complex contract:

```solidity
contract notEmptyContract {
    function sayHello() public pure returns (string memory) {
        return "To whom it may concern, I write you after a long period of silence to alert you that after much reflection, it occurs to me that I don't think you have fully considered...";
    }
}
```

Will have more complex bytecode. In this case, mostly to store the long string present in the return:

```text
608060405234801561001057600080fd5b50610201806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063ef5fb05b14610030575b600080fd5b61003861004e565b60405161004591906100fe565b60405180910390f35b60606040518060e0016040528060ab815260200161012160ab9139905090565b600081519050919050565b600082825260208201905092915050565b60005b838110156100a857808201518184015260208101905061008d565b60008484015250505050565b6000601f19601f8301169050919050565b60006100d08261006e565b6100da8185610079565b93506100ea81856020860161008a565b6100f3816100b4565b840191505092915050565b6000602082019050818103600083015261011881846100c5565b90509291505056fe546f2077686f6d206974206d617920636f6e6365726e2c204920777269746520796f752061667465722061206c6f6e6720706572696f64206f662073696c656e636520746f20616c65727420796f752074686174206166746572206d756368207265666c656374696f6e2c206974206f636375727320746f206d652074686174204920646f6e2774207468696e6b20796f7520686176652066756c6c7920636f6e736964657265642e2e2ea264697066735822122058d68a2853aaa473c9a5ff4dba0cc94657cb2a5a87ce3a986090a7ab991055a464736f6c63430008110033
```

However, if the empty contract inherits from the not empty contract:

```solidity
contract EmptyContract is notEmptyContract {

}
```

The resulting bytecode will include that of the contract inherited from:

```text
608060405234801561001057600080fd5b50610201806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063ef5fb05b14610030575b600080fd5b61003861004e565b60405161004591906100fe565b60405180910390f35b60606040518060e0016040528060ab815260200161012160ab9139905090565b600081519050919050565b600082825260208201905092915050565b60005b838110156100a857808201518184015260208101905061008d565b60008484015250505050565b6000601f19601f8301169050919050565b60006100d08261006e565b6100da8185610079565b93506100ea81856020860161008a565b6100f3816100b4565b840191505092915050565b6000602082019050818103600083015261011881846100c5565b90509291505056fe546f2077686f6d206974206d617920636f6e6365726e2c204920777269746520796f752061667465722061206c6f6e6720706572696f64206f662073696c656e636520746f20616c65727420796f752074686174206166746572206d756368207265666c656374696f6e2c206974206f636375727320746f206d652074686174204920646f6e2774207468696e6b20796f7520686176652066756c6c7920636f6e736964657265642e2e2ea264697066735822122088e486b0a77cd3e2ce809e0a086052815913daec73ebd731e30496d650784f7664736f6c63430008110033
```

---

## Conclusion

In this lesson, you've learned how to use inheritance to include the functionality of one contract in another. You've also learned that inheriting contracts can call `internal` functions, but they cannot call `private` functions. You've also learned that inheriting from a contract adds the size of that contract's bytecode to the total deployed size.

---

[Inheritance]: https://docs.soliditylang.org/en/v0.8.17/contracts.html



<!-- File: ../web/apps/base-docs/base-learn/docs/error-triage/error-triage.md -->

---
title: Error Triage
description: Learn how to identify and resolve common errors in Solidity.
hide_table_of_contents: false
---

Debugging is a part of every language, platform, and framework. The EVM is a unique and relatively constrained computer, so you'll encounter some types of errors that may be unfamiliar. In this article, we'll explore some of the more common ones and share methods for resolving them.

---

## Objectives

By the end of this lesson you should be able to:

- Debug common solidity errors including transaction reverted, out of gas, stack overflow, value overflow/underflow, index out of range, etc.

---

## Compiler Errors

Compiler errors are manifold but almost always very easy to debug, since the error message usually tells you what is wrong and how to fix it.

### Type Errors

You will get a compiler error if you try to assign a literal to the wrong type.

```solidity
// Bad code example, do not use
function compilerTypeError() public pure returns (uint) {
    uint myNumber = "One";
    return myNumber;
}
```

```text
from solidity:
TypeError: Type literal_string "One" is not implicitly convertible to expected type uint256.
 --> contracts/ErrorTriage.sol:8:9:
  |
8 |         uint myNumber = "One";
  |         ^^^^^^^^^^^^^^^^^^^^^
```

Fix by correcting the type or value, as appropriate for your needs:

<details>

<summary>Reveal code</summary>


```solidity
function compilerTypeErrorFixed() public pure returns (string) {
    string myNumber = "One";
    return myNumber;
}
```

</details>

<br/>

### Conversion Errors

Conversion errors occur when you attempt to _implicitly_ convert one type to another. Solidity only allows this under very narrow circumstances where there is no possibility of ambiguous interpretation of the data.

```solidity
// Bad code example, do not use
function compilerConversionError() public pure returns (uint) {
    int8 first = 1;

    return first;
}
```

```text
from solidity:
TypeError: Return argument type int8 is not implicitly convertible to expected type (type of first return variable) uint256.
  --> contracts/ErrorTriage.sol:15:16:
   |
15 |         return first;
   |                ^^^^^
```

Fix by explicitly casting as necessary:

<details>

<summary>Reveal code</summary>


```solidity
function compilerConversionErrorFixed() public pure returns (uint) {
    int8 first = 1;

    return uint(uint8(first));
}
```

</details>

<br/>

:::tip

You'll commonly need to use multiple conversions to bridge from one type to another.

:::

### Operator Errors

You cannot use operators between types as flexibly as you may be used to.

```solidity
// Bad code example, do not use
function compilerOperatorError() public pure returns (uint) {
    int8 first = 1;
    uint256 second = 2;

    uint sum = first + second;

    return sum;
}
```

Operator errors are often paired with a type error.

```text
from solidity:
TypeError: Operator + not compatible with types int8 and uint256.
  --> contracts/ErrorTriage.sol:22:20:
   |
22 |         uint sum = first + second;
   |                    ^^^^^^^^^^^^^^

from solidity:
TypeError: Type int8 is not implicitly convertible to expected type uint256.
  --> contracts/ErrorTriage.sol:22:9:
   |
22 |         uint sum = first + second;
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^
```

Resolve by explicitly converting to the final type:

<details>

<summary>Reveal code</summary>


```
function compilerOperatorErrorFixed() public pure returns (uint) {
    int8 first = 1;
    uint256 second = 2;

    uint sum = uint(uint8(first)) + second;

    return sum;
}
```

</details>

<br/>

### Stack Depth Limit

The [EVM stack] has 1024 slots, but only the top 16 slots are accessible. As a result, you can only have fewer than 16 variables in scope at one time.

:::caution

Other items can also use up these slots. You are **not** guaranteed 15 slots, it can be lower.

:::

```solidity
// Bad code example, do not use
function stackDepthLimit() public pure returns (uint) {
        uint first = 1;
        uint second = 2;
        uint third = 3;
        uint fourth = 4;
        uint fifth = 5;
        uint sixth = 6;
        uint seventh = 7;
        uint eighth = 8;
        uint ninth = 9;
        uint tenth = 10;
        uint eleventh = 11;
        uint twelfth = 12;
        uint thirteenth = 13;
        uint fourteenth = 14;
        uint fifteenth = 15;
        uint sixteenth = 16;

        return first +
                second +
                third +
                fourth +
                fifth +
                sixth +
                seventh +
                eighth +
                ninth +
                tenth +
                eleventh +
                twelfth +
                thirteenth +
                fourteenth +
                fifteenth +
                sixteenth;
    }
```

```text
from solidity:
CompilerError: Stack too deep. Try compiling with --via-ir (cli) or the equivalent viaIR: true (standard JSON) while enabling the optimizer. Otherwise, try removing local variables.
  --> contracts/ErrorTriage.sol:92:17:
   |
92 |                 eighth +
   |                 ^^^^^^
```

Resolve this error by breaking up large functions and separating operations into different levels of scope.

<details>

<summary>Reveal code</summary>


```solidity
function stackDepthLimitFixed() public pure returns (uint) {
    uint subtotalA;
    {
        uint first = 1;
        uint second = 2;
        uint third = 3;
        uint fourth = 4;
        uint fifth = 5;
        uint sixth = 6;
        uint seventh = 7;
        uint eighth = 8;
        subtotalA = first +
            second +
            third +
            fourth +
            fifth +
            sixth +
            seventh +
            eighth;
    }

    uint subtotalB;
    {
        uint ninth = 9;
        uint tenth = 10;
        uint eleventh = 11;
        uint twelfth = 12;
        uint thirteenth = 13;
        uint fourteenth = 14;
        uint fifteenth = 15;
        uint sixteenth = 16;
        subtotalB = ninth +
            tenth +
            eleventh +
            twelfth +
            thirteenth +
            fourteenth +
            fifteenth +
            sixteenth;
    }

    return subtotalA + subtotalB;
}
```

</details>

<br/>

---

## Logical Errors

Logical errors occur when your code is syntactically correct, but still results in a data state that is a violation of the rules of the language.

A [panic] occurs when your code tries to do an illegal operation. These return with a very basic error code, which Remix unfortunately hides. However, it makes up for that annoyance by providing a very powerful debugger.

:::caution

The Remix VM doesn't behave exactly the same as true onchain operations, so note that these errors will not behave exactly the same if triggered while testing with Hardhat, or called from a front end.

:::caution

For each of these examples, copy them into Remix to explore with the debugger on your own.

### Array Index Out-of-Bounds

A panic will be triggered if you try to access an array at an invalid index.

```solidity
// Bad code example, do not use
function badGetLastValue() public pure returns (uint) {
    uint[4] memory arr = [uint(1), 2, 3, 4];

    return arr[arr.length];
}
```

Running this function will result in the following error in the console:

```text
call to ErrorTriage.badGetLastValue errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Note: The called function should be payable if you send value and the value you send should be less than your current balance.
Debug the transaction to get more information.
```

Click the _Debug_ button to open the debugger.

![Debugger](../../assets/images/error-triage/debugger.png)

The debugger contains panels with information about variables in storage, memory, what's on the stack, and so on. You can also add breakpoints to lines of code to further help with debugging.

One of the most useful features is the link near the top instructing you to _"Click here to jump where the call reverted."_

Click that link and the debugger will jump to the point of failure, **and highlight the code that caused the panic.** Neat!

![Highlighted Code](../../assets/images/error-triage/highlight-code.png)

You can find the specific error here, but it's difficult.

Look in the _Memory_ panel. The first item at `0x0` has a hash starting with `0x4e487b71`. This code indicates a panic.

The second item, at `0x20` has the error code of `32` hidden in it, which is for array out-of-bounds.

![Array out-of-bounds](../../assets/images/error-triage/array-out-of-bounds.png)

It's sometimes better to just review the code first to see if the error is obvious.

```solidity
function badGetLastValueFixed() public pure returns (uint) {
    uint[4] memory arr = [uint(1), 2, 3, 4];

    return arr[arr.length-1];
}
```

### Out of Gas

The default settings for Remix make it difficult to trigger an out of gas error because the VM will often crash first. For this example, go to the _Deploy & Run Transactions_ tab and reduce the gas limit to **300000**.

If you write code that can have an ambiguous execution time, it becomes very difficult to accurately estimate gas limits.

In this example, each loop has a 1 in 1000 chance of ending.

:::warning

`block.timestamp` can be manipulated. **DO NOT** use this as a source of randomness if any value can be derived from one outcome over another!

:::

```solidity
// Bad code example, do not use
function badRandomLoop() public view returns (uint) {
    uint seed = 0;
    // DO NOT USE THIS METHOD FOR RANDOM NUMBERS!!! IT IS EASILY EXPLOITABLE!!!
    while(uint(keccak256(abi.encodePacked(block.timestamp, seed))) % 1000 != 0) {
        seed++;
        // ...do something
    }

    return seed;
}
```

Run this function a few times. Often, it will work just fine. Other times, an error appears:

```text
call to ErrorTriage.badLoop errored: VM error: out of gas.

out of gas
	The transaction ran out of gas. Please increase the Gas Limit.

Debug the transaction to get more information.
```

The error message here is a bit misleading. You do **not** usually want to fix this by increasing the gas limit. If you're getting a gas error because the transaction didn't estimate for enough gas, it's better to refactor for better predictability.

```solidity
function badRandomLoopFixed() public view returns (uint) {
    // DO NOT USE THIS METHOD FOR RANDOM NUMBERS!!! IT IS EASILY EXPLOITABLE!!!
    uint times = uint(keccak256(abi.encodePacked(block.timestamp))) % 1000;

    for(uint i = 0; i <= times; i++) {
        // ...do something
    }

    return times;
}
```

### Overflow or Underflow

The `uint` type will _panic_ in the event of an overflow or underflow.

```solidity
function badSubtraction() public pure returns (uint) {
    uint first = 1;
    uint second = 2;
    return first - second;
}
```

As before, you can see the panic code and panic type in _memory_.

![Underflow](../../assets/images/error-triage/underflow.png)

In this case, the error type is `11`, for overflow/underflow outside of an `unchecked` block.

Fix by changing your code to handle the expected range of values.

<details>

<summary>Reveal code</summary>


```solidity
function badSubstractionFixed() public pure returns (int) {
    int first = 1;
    int second = 2;
    return first - second;
}
```

</details>

<br/>

### Divide by Zero

Divide by zero errors also trigger a panic, with a code of `12`.

```solidity
function badDivision() public pure returns (uint) {
    uint first = 1;
    uint second = 0;
    return first / second;
}
```

![Divide by zero](../../assets/images/error-triage/divide-by-zero.png)

Don't divide by zero.

---

## Conclusion

In this lesson, you reviewed the causes of and solutions for a number of compiler errors and logical errors that you may encounter.

---

[panic]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html?#panic-via-assert-and-error-via-require
[EVM stack]: https://docs.soliditylang.org/en/v0.8.17/introduction-to-smart-contracts.html#storage-memory-and-the-stack



<!-- File: ../web/apps/base-docs/base-learn/docs/error-triage/error-triage-vid.md -->

---
title: Error Triage
description: Learn to debug common errors.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='817805593' title='Error Triage' />



<!-- File: ../web/apps/base-docs/base-learn/docs/error-triage/error-triage-exercise.md -->

---
title: Error Triage Exercise
description: Exercise - Demonstrate your debugging skill.
hide_table_of_contents: false
---

Copy the starter code into a new file in Remix.

Debug the existing functions in the provided contract.

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract ErrorTriageExercise {
    /**
     * Finds the difference between each uint with it's neighbor (a to b, b to c, etc.)
     * and returns a uint array with the absolute integer difference of each pairing.
     */
    function diffWithNeighbor(
        uint _a,
        uint _b,
        uint _c,
        uint _d
    ) public pure returns (uint[] memory) {
        uint[] memory results = new uint[](3);

        results[0] = _a - _b;
        results[1] = _b - _c;
        results[2] = _c - _d;

        return results;
    }

    /**
     * Changes the _base by the value of _modifier.  Base is always >= 1000.  Modifiers can be
     * between positive and negative 100;
     */
    function applyModifier(
        uint _base,
        int _modifier
    ) public pure returns (uint) {
        return _base + _modifier;
    }

    /**
     * Pop the last element from the supplied array, and return the popped
     * value (unlike the built-in function)
     */
    uint[] arr;

    function popWithReturn() public returns (uint) {
        uint index = arr.length - 1;
        delete arr[index];
        return arr[index];
    }

    // The utility functions below are working as expected
    function addToArr(uint _num) public {
        arr.push(_num);
    }

    function getArr() public view returns (uint[] memory) {
        return arr;
    }

    function resetArr() public {
        delete arr;
    }
}

```

---

## Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={10}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/structs/structs-exercise.md -->

---
title: Structs Exercise
description: Exercise - Demonstrate your knowledge of structs.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a contract called `GarageManager`. Add the following in storage:

- A public mapping called `garage` to store a list of `Car`s (described below), indexed by address

Add the following types and functions.

### Car Struct

Implement a `struct` called `Car`. It should store the following properties:

- `make`
- `model`
- `color`
- `numberOfDoors`

### Add Car Garage

Add a function called `addCar` that adds a car to the user's collection in the `garage`. It should:

- Use `msg.sender` to determine the owner
- Accept arguments for make, model, color, and number of doors, and use those to create a new instance of `Car`
- Add that `Car` to the `garage` under the user's address

### Get All Cars for the Calling User

Add a function called `getMyCars`. It should return an array with all of the cars owned by the calling user.

### Get All Cars for Any User

Add a function called `getUserCars`. It should return an array with all of the cars for any given `address`.

### Update Car

Add a function called `updateCar`. It should accept a `uint` for the index of the car to be updated, and arguments for all of the `Car` types.

If the sender doesn't have a car at that index, it should revert with a custom `error` `BadCarIndex` and the index provided.

Otherwise, it should update that entry to the new properties.

### Reset My Garage

Add a public function called `resetMyGarage`. It should delete the entry in `garage` for the sender.

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={7}/>
  
<br/>
<details>
  <summary>
    ⚠️ Spoiler Alert: Open only if tests fail</summary>

Ensure your variable sizes align with their intended use, and consider the nuances of packing in Solidity. Resources: [Solidity - Layout in Storage](https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html#layout-of-state-variables-in-storage), [Variables in Struct](https://docs.base.org/base-learn/docs/structs/structs-sbs#setting-up-the-struct)

</details>



<!-- File: ../web/apps/base-docs/base-learn/docs/structs/structs-sbs.md -->

---
title: Structs
description: Practice using structs.
hide_table_of_contents: false
---

The `struct` type allows you to organize related data of different types.

---

## Objectives

By the end of this lesson you should be able to:

- Construct a `struct` (user-defined type) that contains several different data types
- Declare members of the `struct` to maximize storage efficiency
- Describe constraints related to the assignment of `struct`s depending on the types they contain

---

## Creating a Struct

In the last exercise, we used a `mapping` to create a relationship between an `address` and a `uint`. But what if your users have favorite colors too? Or favorite cars? You **could** create a `mapping` for each of these, but it would quickly get awkward. Instead, a [`struct`] can be used to create a custom type that can store all of a user's favorites within one data type.

Create a new contract called `Structs`.

### Setting up the Struct

Instantiate a `struct` with the keyword, followed by a name for the type, curly brackets, and the variables that make up the type. Add a stub for `Favorites`:

```solidity
struct Favorites {

}
```

After consulting with the designers, we need to store the following for each address's favorites:

- Favorite number
- Birth Day of Month
- Favorite color
- Lucky Lottery numbers

Let's pause for a moment and do some technical design around how to save our favorites.

The product team has confirmed for us that we can safely expect that no users have a favorite number greater than 65,536, and of course, everyone is born on a day of the month between 1-31.

Variable [packing] also works inside structs, so we could potentially save on storage by using smaller `uint`s for those variables. However, people don't change their favorite number very often, and the day of the month that they were born on never changes.

Therefore, it's probably more gas-efficient and less cumbersome to write other parts of the code, if we just use `uint` for both variables.

Favorite color can be a `string`.

For Lucky Lottery Numbers, we need a collection. We could use a dynamic array, since this will be in _storage_, but we already know that the lottery has 5 numbers.

Try to use this information to build the `struct` on your own. You should end up with something similar to:

<details>

<summary>Reveal code</summary>

```solidity
struct Favorites {
    uint favoriteNumber;
    uint birthDay;
    string favoriteColor;
    uint[5] lotteryNumbers;
}
```

</details>

<br/>

### Instantiating a Struct with Its Name

There are two ways to instantiate a struct using its name. The first is similar to instantiating a new object in JavaScript:

```solidity
Favorites memory myFavorites = Favorites({
    favoriteNumber: 29,
    birthDay: 14,
    favoriteColor: "red",
    lotteryNumbers: [uint(1), 2, 3, 4, 5]
});
```

You can also use a shorthand method where you skip the member names and just list a value for each one. Note that the curly brackets are **not** included in this format:

```solidity
Favorites memory myFavorites = Favorites(
    29,
    14,
    "red",
    [uint(1), 2, 3, 4, 5]
);
```

There's no difference in gas costs with either of these methods. Use the one that makes the most sense for the given situation.

### Saving Multiple Instances to Storage

Next, we need to figure out the best way to organize the `Favorites` in _storage_. There are a few options, as always, each with tradeoffs. You could match the pattern you used for favorite numbers and utilize a `mapping` to match `addresses` to `Favorites`.

Another popular method is to use an array, which takes advantage of `.push` returning a reference to the newly added element, and the fact that the concept of _undefined_ does not exist in Solidity.

First, instantiate an array of `Favorites`:

```solidity
Favorites[] public userFavorites;
```

Next, add a `public` function to add submitted favorites to the list. It should take each of the members as an argument. Then, assign each argument to the new element via the reference returned by `push()`.

<details>

<summary>Reveal code</summary>

```solidity
function addFavorite(
    uint _favoriteNumber,
    uint _birthDay,
    string calldata _favoriteColor,
    uint[5] calldata _lotteryNumbers
) public {
    // .push() returns a reference to the new element
    Favorites storage newFavorite = userFavorites.push();
    newFavorite.favoriteNumber = _favoriteNumber;
    newFavorite.birthDay = _birthDay;
    newFavorite.favoriteColor = _favoriteColor;
    newFavorite.lotteryNumbers = _lotteryNumbers;
}
```

</details>

<br/>

Alternatively, you can create an instance in memory, then `push` it to storage.

<details>

<summary>Reveal code</summary>

```solidity
function addFavorite(
    uint _favoriteNumber,
    uint _birthDay,
    string calldata _favoriteColor,
    uint[5] calldata _lotteryNumbers
) public {
    Favorites memory myFavorites = Favorites(
        29,
        14,
        "red",
        [uint(1), 2, 3, 4, 5]
    );

    userFavorites.push(myFavorites);
}
```

</details>

<br/>

The gas cost is similar for each of these methods.

---

## Unexpected Behavior in Structs

Structs in Solidity exhibit some properties that are unexpected, or even frustrating. Working with them often includes untangling a set of mutually-exclusive properties and needs.

### Dynamic Storage Arrays in Structs

The product team has contacted you to let you know that the beta testers are complaining about the `lotteryNumbers`. As it turns out, not every locality has lotteries where 5 numbers are drawn. Some have 3, 4, or even 6!.

You might think this is an easy enough change. After all, you can just remove the size from the array declaration inside `Favorites`. Go ahead and try it:

```solidity
struct Favorites {
    uint favoriteNumber;
    uint birthDay;
    string favoriteColor;
    uint[] lotteryNumbers; // Removed the '5'
}
```

You'll get an error if you're using the `memory` method shown above.

```text
from solidity:
TypeError: Invalid type for argument in function call. Invalid implicit conversion from uint256[5] memory to uint256[] memory requested.
  --> contracts/mappings_exercise.sol:70:13:
   |
70 |             [uint(1), 2, 3, 4, 5]
   |             ^^^^^^^^^^^^^^^^^^^^^
```

The simplest resolution here is to switch back to using `push()` to create an empty instance of `Favorites`, then assigning the values.

The reason this works is a little obtuse. In the failing example, an unsized `uint` array is the expected type for the argument, but a sized `uint` array is provided. Solidity cannot perform implicit conversions like this most of the time and you'll get a compiler error if you provide the wrong type for an argument, even if it is convertible.

One exception to this rule is that Solidity **can** perform an implicit conversion during _assignment_ if the variable on the right side "fits" into the variable on the left side.

`uint[5]` fits in `uint[]`, so Solidity will allow it to sit 🐈.

But what happens if you use the _getter_ for `userFavorites` to retrieve your entry?

```text
{
	"0": "uint256: favoriteNumber 29",
	"1": "uint256: birthDay 14",
	"2": "string: favoriteColor red"
}
```

What happened to the array? It's not there, and it turns out that this is [on purpose].

### Mappings Inside of Structs

You may add `mappings` inside of `struct`s, subject to a few quirks and restrictions. Add `mapping (uint => uint) numberPairs;` to `Favorites`.

In `addFavorites`, assign `newFavorite.numberPairs[33] = 66;`

Deploy and test. So far, so good!

_Déjà vu_ ahead: But what happens if you use the _getter_ for `userFavorites` to retrieve your entry?

```text
{
	"0": "uint256: favoriteNumber 29",
	"1": "uint256: birthDay 14",
	"2": "string: favoriteColor red"
}
```

It's not there, and it turns out that this is [on purpose].

Another issue emerges if you try to return the struct from a public function. What if you wanted your `addFavorite` function to return a reference to the new favorite?

```solidity
// Bad code example, will not work
function addFavorite(
    uint _favoriteNumber,
    uint _birthDay,
    string calldata _favoriteColor,
    uint[] calldata _lotteryNumbers
) public returns (newFavorite memory) {
    // .push() returns a reference to the new element
    Favorites storage newFavorite = userFavorites.push();
    newFavorite.favoriteNumber = _favoriteNumber;
    newFavorite.birthDay = _birthDay;
    newFavorite.favoriteColor = _favoriteColor;
    newFavorite.lotteryNumbers = _lotteryNumbers;
    newFavorite.numberPairs[33] = 66;

    return newFavorite;
}
```

You'll get an error. The `mapping` type cannot be returned by a `public` or `external` function, so neither can a `struct` that contains one.

```text
from solidity:
TypeError: Types containing (nested) mappings can only be parameters or return variables of internal or library functions.
  --> contracts/mappings_exercise.sol:64:23:
   |
64 |     ) public returns (Favorites memory) {
   |                       ^^^^^^^^^^^^^^^^
```

Finally, what happens if you try to assign `newFavorite` to a `memory` variable? Again, an error occurs because `mapping`s can only be in `storage`.

```solidity
// Bad code example, will not work
Favorites memory secondFavorite = newFavorite;
```

```text
from solidity:
TypeError: Type struct Structs.Favorites memory is only valid in storage because it contains a (nested) mapping.
  --> contracts/mappings_exercise.sol:82:9:
   |
82 |         Favorites memory secondFavorite = newFavorite;
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

### Automatic Getters for Public Structs

As with other types, if you put a `public` `struct` in storage at the contract level, the compiler will generate a getter automatically. However, these don't work quite the way you might expect. For example, imagine:

```solidity

struct MyStruct {
    uint first;
    uint second;
    uint third;
}

MyStruct myStruct;

```

The automatic getter for `myStruct` will **not** be:

```solidity
// Approximate example, not real code
function myStruct() public view returns (MyStruct memory) {
    return myStruct;
}
```

Instead, it returns the members individually:

```solidity
// Approximate example, not real code
function myStruct() public view returns (uint, uint, uint) {
    return (myStruct.first, myStruct.second, myStruct.third);
}
```

Create your own getter to return the data as a tuple, which will be interpreted as the appropriate type if it's called from another contract via an interface.

```solidity
function getMyStruct() public view returns (MyStruct memory) {
    return myStruct;
}
```

---

## Conclusion

In this lesson, you've learned how to use the `struct` keyword to create a custom type that stores related data. You've also learned three methods of instantiating them and common patterns for storing `struct`s in storage. Finally, you've explored some of the constraints that emerge when working with more complex data types within a `struct`.

[`struct`]: https://docs.soliditylang.org/en/v0.8.17/types.html#structs
[packing]: https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html
[on purpose]: https://github.com/ethereum/solidity/issues/1626



<!-- File: ../web/apps/base-docs/base-learn/docs/structs/structs-vid.md -->

---
title: Structs
description: Create user-defined types.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479292' title='Structs' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-ethereum/ethereum-dev-overview-vid.md -->

---
title: Ethereum Applications
description: An overview of web 3 application development.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='808101737' title='Ethereum Applications Overview' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-ethereum/evm-diagram.md -->

---
title: EVM Diagram
description: An overview of the Ethereum Virtual Machine
hide_table_of_contents: false
---

In this article, we'll examine the inner workings of the EVM, its components, and its role within the Ethereum network.

---

## Objectives

By the end of this lesson you should be able to:

- Diagram the EVM

---

## What is the EVM?

The Ethereum Virtual Machine (EVM) is the core engine of Ethereum. It is a Turing-complete, sandboxed virtual machine designed to execute smart contracts on the network. The term "sandboxed" means that the EVM operates in an isolated environment, ensuring that each smart contract's execution does not interfere with others or the underlying blockchain. As we've learned, the EVM's Turing-complete nature allows developers to write complex programs that can perform any computationally feasible task.

The EVM employs a sophisticated resource management system using gas to regulate computation costs and prevent network abuse. It also supports a rich ecosystem of onchain apps by providing a versatile set of opcodes for smart contract logic, and fostering interoperability with various programming languages, tools, and technologies. This adaptability has made the EVM a fundamental component in the advancement and growth of the Ethereum network.

---

## EVM Components

The EVM has several key components that enable it to process and manage smart contracts. Let's define them:

- **World State:** Represents the entire Ethereum network, including all accounts and their associated storage.
- **Accounts:** Entities that interact with the Ethereum network, including Externally Owned Accounts (EOAs) and Contract Accounts.
- **Storage:** A key-value store associated with each contract account, containing the contract's state and data.
- **Gas:** A mechanism for measuring the cost of executing operations in the EVM, which protects the network from spam and abuse.
- **Opcodes:** Low-level instructions that the EVM executes during smart contract processing.
- **Execution Stack:** A last-in, first-out (LIFO) data structure for temporarily storing values during opcode execution.
- **Memory:** A runtime memory used by smart contracts during execution.
- **Program Counter:** A register that keeps track of the position of the next opcode to be executed.
- **Logs:** Events emitted by smart contracts during execution, which can be used by external systems for monitoring or reacting to specific events.

---

## EVM Execution Model

In simple terms, when a transaction is submitted to the network, the EVM first verifies its validity. If the transaction is deemed valid, the EVM establishes an execution context that incorporates the current state of the network and processes the smart contract's bytecode using opcodes. As the EVM runs the smart contract, it modifies the blockchain's world state and consumes gas accordingly. However, if the transaction is found to be invalid, it will be dismissed by the network without further processing. Throughout the smart contract's execution, logs are generated that provide insights into the contract's performance and any emitted events. These logs can be utilized by external systems for monitoring purposes or to respond to specific events.

![EVM Execution Model](../../assets/images/ethereum-virtual-machine/evm-execution-basic.png)

---

## Gas and Opcode Execution

While we have already delved into the concept of gas in a previous lesson, it is worth reiterating its critical role within the EVM and as a fundamental component of Ethereum. Gas functions as a metric for quantifying the computational effort needed to carry out operations in the EVM. Every opcode in a smart contract carries a specific gas cost, which reflects the computational resources necessary for its execution.

Opcodes are the low-level instructions executed by the EVM. They represent elementary operations that allow the EVM to process and manage smart contracts.

![Opcode Execution](../../assets/images/ethereum-virtual-machine/opcode-execution.png)

During execution, the EVM reads opcodes from the smart contract, and depending on the opcode, it may update the world state, consume gas, or revert the state if an error occurs. Some common opcodes include:

- **ADD:** Adds two values from the stack.
- **SUB:** Subtracts two values from the stack.
- **MSTORE:** Stores a value in memory.
- **SSTORE:** Stores a value in contract storage.
- **CALL:** Calls another contract or sends ether.

---

## Stack and Memory

The EVM stack and memory are critical components of the EVM architecture, as they enable smart contracts to manage temporary data during opcode execution. The stack is a last-in, first-out (LIFO) data structure that is used for temporarily storing values during opcode execution. It is managed by the EVM and is separate from the contract's storage. The stack supports two primary operations: push and pop.

The push operation adds a value to the top of the stack, while the pop operation removes the top value from the stack. These operations are used to manage temporary data during opcode execution. For example, an opcode that performs an addition operation might push the two operands onto the stack, perform the addition, and then pop the result off the top of the stack.

During contract execution, memory serves as a collection of bytes, organized in an array, for the purpose of temporarily storing data. It can be read from and written to by opcodes. Memory is often used to store temporary data during opcode execution, such as when working with dynamically sized data like strings or arrays that are being manipulated or computed within the smart contract before being stored in the contract's storage. When a smart contract needs to store temporary data during opcode execution, it can use the memory to store that data.

![EVM Stack and Memory](../../assets/images/ethereum-virtual-machine/evm-stack-memory.png)

---

## EVM Architecture and Execution Context

To understand the inner workings of the EVM, the following diagram offers a streamlined visualization of its transaction execution process. It begins with the transaction initiation, and progresses to the gas computations for each operation. Integral to the process are the EVM's stack, memory, and storage, which are engaged to manage and persist data throughout the lifecycle of a transaction. Checks and validations at each step ensure the validity of operations, safeguarding the network's integrity. This systemized sequence of actions forms the bedrock of transaction and smart contract execution, ensuring Ethereum's consistent and secure operation.

![EVM architecture and execution context](../../assets/images/ethereum-virtual-machine/evm-architecture-execution.png)
:::info
**Data Bytecode in the EVM**

Every transaction or smart contract call within the EVM uses "bytecode", which
is a sequence of instructions that guides the EVM's actions. Bytecode is
primarily presented in a compact hexadecimal format.

---

Decoding the example sequence: `0x6080604052`

```go
60 // PUSH1: Pushes the next byte (0x80) onto the stack.
80 // The byte to be pushed onto the stack by the previous PUSH1.
60 // PUSH1: Pushes the next byte (0x40) onto the stack.
40 // The byte to be pushed onto the stack by the previous PUSH1.
52 // MSTORE: Stores the second stack item in memory at the address of the first.
```

This bytecode sequence is not a random set of characters. Each segment corresponds to specific operations or data in the EVM. Opcodes dictate actions, while subsequent data provides specifics.
:::

---

## Conclusion

The EVM plays a vital role within the Ethereum network. By examining the EVM's key components as well as its architecture and execution model, we've gained insight into the engine of Ethereum and how it enables the smooth execution of smart contracts on the platform.

---

## See Also

- [The Ethereum Virtual Machine (Mastering Ethereum)](https://cypherpunks-core.github.io/ethereumbook/13evm.html#evm_architecture)
- [Ethereum Virtual Machine (Ethereum docs)](https://ethereum.org/en/developers/docs/evm/)

<!-- Reference Style Links -->

[the ethereum virtual machine (mastering ethereum)]: https://cypherpunks-core.github.io/ethereumbook/13evm.html#evm_architecture



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-ethereum/ethereum-applications.md -->

---
title: Ethereum Applications
description: An overview of the development ethos of Ethereum, applications built on its network, and a high-level comparison of Web2 and Web3
hide_table_of_contents: false
---

In this article, we'll explore Ethereum's significance and impact in the crypto ecosystem as well as its role in shaping the Web3 landscape. We'll learn about Ethereum's ethos and goals and also examine the different types of applications developed on Ethereum. Lastly, we'll take a look at the evolution of the web with an emphasis on comparing Web2 and Web3 development.

---

## Objectives

By the end of this lesson you should be able to:

- Describe the origin and goals of the Ethereum blockchain
- List common types of applications that can be developed with the Ethereum blockchain
- Compare and contrast Web2 vs. Web3 development
- Compare and contrast the concept of "ownership" in Web2 vs. Web3

---

## The Ethos and Goals of Ethereum

Ethereum was originally proposed in 2013 by Vitalik Buterin, who was then a young developer in the Bitcoin community. Vitalik had a vision that the potential of blockchain technology extended far beyond a decentralized digital currency. When his ideas were rejected by the Bitcoin community, he set out to create a platform that could bring his vision to life.

The ethos of Ethereum is fundamentally different from Bitcoin's. Bitcoin development is conservative; it's focused on maintaining the existing protocol, making only incremental improvements over time rather than implementing radical changes. In other words, changes are slow and deliberate and any unnecessary risk-taking is generally frowned upon. Ethereum development, on the other hand, is focused on innovation and experimentation. There is more of a willingness to take risks and make radical changes to the protocol in order to improve on and expand upon functionality and enable new use cases.

Ethereum's primary goal is to be a general, all-purpose blockchain that allows developers to create any type of decentralized application that their minds can conjure up. One of the most important features that unlock all of these possibilities is smart contracts. Without smart contract functionality, most applications built on the platform today would be nonexistent.

![Bitcoin & Ethereum Comparison](../../assets/images/introduction-to-ethereum/btc-eth-comparison.png)

---

## Applications on Ethereum

Before delving into the different types of applications built on Ethereum, let's review one of the underlying forces of the smart contracts that make them possible.

### Scripting

As we've learned, one of Bitcoin's limitations when it comes to complex applications being built on the protocol is scripting. Its simple stack-based, left-to-right scripting system lacks the flexibility to support smart contracts. In the Ethereum whitepaper, Vitalik pointed out several limitations to Bitcoin scripting. A couple of key ones to note are:

- Lack of Turing-completeness. Although this is an intentional feature of Bitcoin to avoid infinite loops during transaction verification, without loops or recursion, running a complex program that a decentralized application demands, is not possible.

- Lack of state. Bitcoin's UTXO model only allows for simple contracts and not the complex stateful contracts needed for most decentralized applications. What that means is that there is no internal state beyond a UTXO being spent or unspent.

Ethereum's scripting languages, most notably Solidity, are Turing-complete and stateful, among other features. These features allow smart contracts to be executed deterministically, meaning that the outcome of the contract is predictable and can be enforced automatically and autonomously. They also allow developers to write much more complex programs that can execute a much wider range of operations.

It is this flexibility and versatility in Ethereum's scripting that ultimately powers the decentralized applications that we know.

### Decentralized Finance (DeFi)

DeFi is one of the most popular use cases for Ethereum. In DeFi Summer 2020, we saw an explosion in the usage and popularity of DeFi applications built on Ethereum. During this brief period alone, the total value locked in DeFi protocols increased from less than $1 billion to more than $10 billion. This period marked a turning point, as it brought more attention to the space, and it solidified Ethereum as the de facto smart contract platform of the DeFi and greater Web3 ecosystem.

DeFi applications are designed to provide traditional financial services, such as lending, borrowing, trading, and much more, in a transparent, open and accessible manner. All of these services are facilitated by smart contracts.

How exactly does this work? Let's take a look at a simple example in the context of a DeFi lending platform, such as Aave or Compound.

Suppose Alice wants to borrow 5 ETH but doesn't want to sell her 10,000 USDC. She can deposit that USDC as collateral and borrow 5 ETH against it.

First, Alice must interact with the smart contract of the platform. The smart contract will check if Alice has 10,000 USDC in her wallet and, if so, will lock it up as collateral for the loan. The smart contract then transfers 5 ETH to Alice's wallet. The smart contract will also define the terms of the loan, such as the interest rate and the repayment date.

Alice now has 5 ETH that she can use for whatever she wants. However, she must repay the loan within the specified period. If Alice repays the loan on time, the smart contract will release her deposited collateral back to her. Otherwise, it will automatically liquidate her collateral and transfer it to the lender's address in exchange for the 5 ETH that was lent to her. The repayment will also include any accrued interest based on the interest rate set by the smart contract.

In this way, smart contracts enable DeFi platforms to operate autonomously without a centralized entity. The smart contract provides security and transparency to both the borrower and the lender, as the terms of the loan are defined in the code and enforced automatically.

Of course, this does not mean that DeFi comes without risks. Although it's beyond the scope of this article, it's worth mentioning that DeFi has been the target of numerous smart contract exploits involving hundreds of millions of dollars in value.

### Non-Fungible Token (NFT)

NFTs are another application of Ethereum that has gained significant attention in recent years. NFTs are unique digital assets that represent ownership of a specific item. They can be used to represent just about anything, but most notably digital artwork, sports collectibles, and in-game items.

Smart contracts play a crucial role in NFTs by providing a way to represent and enforce ownership of the digital asset. When a new NFT is created, a smart contract is deployed on Ethereum that defines the unique characteristics of that asset as well as the ownership information and rules for transferring ownership.

Ethereum's ERC-721 standard was the first to introduce NFTs in 2017, and it has since become the most popular standard for creating and trading NFTs on Ethereum.

We'll cover more on tokens and token standards for fungible and non-fungible assets later on in the course.

### Decentralized Autonomous Organization (DAO)

DAOs are another common use case for Ethereum and also one of the earliest use cases implemented on the network. In simple words, DAOs are software-enabled, community-led organizations. They allow a community to pool resources toward a shared goal, such as [buying one of the original copies of the U.S. Constitution](https://www.theverge.com/22820563/constitution-meme-47-million-crypto-crowdfunding-blockchain-ethereum-constitution) or determining the future of a protocol. Because DAOs aren't tied to a physical location, they are able to mobilize quickly and
attract resources and capital from all over the world.

The rules of a DAO are established by community members through the use of smart contracts, which lay the groundwork for how a DAO operates. When a new DAO is created, a contract is deployed to the network. It contains the rules that govern the organization, including how its resources are managed. Members of the DAO can then interact with the contract by sending transactions to the blockchain.

DAOs typically use a token-based system to govern voting and decision-making. Members of the DAO are issued tokens that represent their ownership and influence within the organization. These tokens can be used to vote on proposals and allocate resources.

When a proposal is submitted to the DAO, members can vote on whether to accept or reject it. The smart contract tracks the votes and automatically executes the proposal if it receives enough support from the members. This process allows members of the DAO to collectively make decisions and take actions in a decentralized way.

### Other Applications

While the above use cases have been the most prominent applications on Ethereum, there are a plethora of others, including:

- **Identity Management** is one use case that has come to the forefront in recent years. The most notable example is the Ethereum Name Service (ENS). It allows users to register human-readable domain names, similar to the traditional DNS system, but with the added functionality of being able to associate Ethereum and other blockchain addresses with a domain name, such as `vitalik.eth`. This makes it easier for users to send and receive transactions without having to remember or type in long and complex addresses.

- **Gaming** is another common use case. Axie Infinity and Decentraland are both popular examples of decentralized games that make use of fungible and non-fungible tokens for a variety of purposes.

- **Prediction markets** are another use case where users can bet on the outcome of real-world events, such as forecasting election results or predicting which team will win a game. Augur and Gnosis are popular examples of this application.

There are many other use cases from supply chain, energy, and intellectual property management to decentralized storage and content management to governance and voting systems. The list goes on and on, and it's worth taking some time to explore these types of applications on your own.

---

## Evolution of the Web

Opinions abound in the history, divisions, and eras of the development and evolution of the internet. One popular explanation divides the web into three major eras (so far).

#### Web1

The web has come a long way since its humble read-only beginnings in the early 1990s. Web1 is often referred to as the _static web_, meaning it was primarily a collection of static web pages that provided information to users with limited interaction and dynamic content.

#### Web2

In the early 2000s, a _dynamic web_ emerged. Web2 introduced more interactive and dynamic content, such as social media and e-commerce. It's characterized by the use of centralized servers that store and control user data. In other words, with Web2, users can interact with content, share information, and collaborate with others, but they have limited control over their data. A vast majority of the web today operates in this paradigm.

#### Web3

Web3 or the _decentralized web_ is the next phase of the web that has started to emerge in recent years with the rise in popularity of Ethereum. This iteration of the web is focused on user ownership and control over data, providing a more private, decentralized, and secure web experience.

### The Limitations of Web2

While Web2 brought many benefits beyond its predecessor, there are some key limitations to consider.

- **Privacy & Control:** Users have limited control over their data and how it is used. Companies often have broad or even complete control over user data on a given platform.

- **Censorship:** Due to centralized control of user data, corporations or governments can censor content they deem as inappropriate or dangerous, which can limit free speech and expression or block access to certain online services. This is especially concerning in countries with authoritarian regimes, which often use censorship as a tool to control citizens and maintain power.

- **Lack of transparency:** Users cannot always verify how their data is being used or who has access to it.

- **Security vulnerabilities:** Because Web2 relies on centralized servers, it is more vulnerable to hacking and data breaches, which can expose sensitive user information and compromise online safety.

- **Limited interoperability:** Most Web2 platforms are not interoperable, meaning that different platforms may not be compatible with each other. Data is generally confined to one system.

### The Limitations of Web3

While many of the limitations of Web2 have spurred the development of Web3 by aiming to provide a more decentralized, secure, and private web, Web3 does not come without its own set of limitations.

- **Speed:** The reliance on decentralized networks and consensus mechanisms result in much slower processing times compared to centralized systems.

- **Storage:** Storing data onchain can be very expensive, which can make it challenging for developers to create apps that require large amounts of storage.

- **Smart contract limitations:**

  - Smart contracts on Ethereum are currently limited to a maximum size of 24 KB, which can limit the complexity of the logic that can be programmed into them.

  - Once a smart contract is deployed, it cannot be updated or changed. If there is a bug or a flaw in the contract, it cannot be fixed unless a new contract is deployed.

- **All data is public:** The transparency of blockchain means that all data is public and visible to anyone. While this can be an advantage in terms of transparency and accountability, it can also be a limitation for applications that may require privacy or confidentiality.

![Web2 & Web3 Limitations](../../assets/images/introduction-to-ethereum/web2-web3-limitations.png)

### Web2 vs Web3 Development

While there are many general distinctions to be made between Web2 and Web3, these characteristics are even more apparent when examining their development approaches.

#### Web2

In Web2, engineering is centered around a client-server architecture, and development is focused on building applications for specific platforms and using APIs and tools provided by those platforms to create user interfaces and access data. There is a top-down corporate approach to development processes, and code is generally proprietary and closed-sourced. As a result, there tends to be very limited collaboration with developers outside of a company and there is little integration between different platforms.

Web2 developers rely on centralized infrastructure, such as servers and cloud-computing services provided by large tech companies to host their applications and store data. This creates a centralized system where the platforms and companies that control the infrastructure have significant power and control over the applications and data that are built on top of them.

#### Web3

In contrast, the Web3 development paradigm is centered around a distributed architecture, where developers build applications that run on decentralized protocols and smart contracts. There is a bottom-up community approach to development processes, and there is an emphasis on open-source code and open standards. Web3 development culture is collaborative, and there is strong integration and interoperability between platforms.

Web3 development requires a different set of engineering skills and tools. Developers need to have a strong understanding of blockchain technology, cryptography, and distributed systems, and they also need to be proficient in programming languages like Solidity.

There is also a different approach to testing and deployment. Because onchain apps run on distributed systems, developers need to consider factors like network latency and the possibility of network partitions. They also need to ensure that their applications are extremely secure and resistant to a variety of attacks because the stakes can often be very high when it comes to dealing with millions and even billions of dollars of value that cannot be recovered in the event of a hack. Developers also have to consider concepts like immutability because once code is deployed to a blockchain, it cannot be edited.

Overall, Web3 development requires a different set of engineering skills and tools as well as a deeper understanding of distributed systems and cryptography. Developers also need the ability to think creatively about how to build applications that are constrained by the technical limitations of the Web3 paradigm, such as speed, storage, and scalability.

![Web2 vs Web3 Development](../../assets/images/introduction-to-ethereum/web2-web3-development.png)

---

## Conclusion

Ethereum was created to extend the potential of blockchain technology beyond just a decentralized digital currency platform. Its ethos of innovation and experimentation has made a major impact on shaping the crypto ecosystem and has played a significant role in shaping the landscape of Web3. The use of smart contracts has enabled a wide range of new web applications, including DeFi, NFTs, DAOs, and many more.

The evolution of the web has brought us from a static Web1 to a dynamic Web2, and now to a decentralized Web3. While Web2 brought many key benefits, it also came with many drawbacks regarding privacy, censorship, and security vulnerabilities. Web3 aims to address these challenges but has its own set of limitations. Lastly, the development paradigms of Web2 and Web3 are distinct in their architecture, infrastructure, and their development approaches. Web3 development requires a different set of skills and a different mental framework from its predecessor.

---

## See also

- [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)
- [Decentralized Applications (Dapps)](https://ethereum.org/en/dapps/)
- [Web2 vs Web3](https://ethereum.org/en/developers/docs/web2-vs-web3/)
- [The Architecture of a Web 3.0 Application](https://www.preethikasireddy.com/post/the-architecture-of-a-web-3-0-application)

<!-- Reference Style Links -->

[Ethereum Whitepaper]: https://ethereum.org/en/whitepaper/



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-ethereum/intro-to-ethereum-vid.md -->

---
title: Introduction
description: Welcome to the world of blockchain development!
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='813631865' title='Intro to Ethereum' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-ethereum/gas-use-in-eth-transactions.md -->

---
title: Gas Use in Ethereum Transactions
description: An overview of how gas works in Ethereum
hide_table_of_contents: false
---

In this article, we'll delve into the concept of gas and its importance in the Ethereum ecosystem. You'll learn why Ethereum relies on a system of gas to regulate the execution of transactions and smart contracts, and how it plays a crucial role in the proper functioning of the network.

---

## Objectives

By the end of this lesson you should be able to:

- Explain what gas is in Ethereum
- Explain why gas is necessary in Ethereum
- Understand how gas works in Ethereum transactions

---

## What is gas?

Gas is a term used in Ethereum to describe a computational unit that measures the amount of computational work needed to perform specific operations on the network. Unlike Bitcoin, where transaction fees only consider the size of a transaction, Ethereum accounts for every computational step performed by transactions and smart contract code execution. In other words, every single operation that is performed on Ethereum requires a certain amount of gas.

### Complexity

The amount of gas required for an operation depends on its complexity. More complex operations require more computational resources and therefore require more gas to be executed. For example, a simple transaction that involves sending ETH from one address to another may require less gas than a complex smart contract that executes multiple operations or interacts with multiple other contracts.

### State of the Network

Gas costs can also vary depending on the state of the network, or more specifically, how congested it is. When there are more transactions waiting to be processed than the network can handle, it will prioritize transactions based on the gas price that was set by the user, meaning that higher gas prices are more likely to get processed first. When the network is congested, gas prices increase to encourage more efficient use of the network's resources and decrease when network usage is lower. This dynamic pricing mechanism ensures that the Ethereum network remains accessible and functional for all users, while also incentivizing responsible and efficient use of the network's resources.

![Gas Costs vs Network Congestion](../../assets/images/introduction-to-ethereum/gas-costs.png)

---

## Why is gas necessary?

### Turing Completeness

As we've learned, Ethereum is a Turing-complete platform, which means that any program that can be represented in code can theoretically be expressed and executed on the network. This opens up the door to countless different types of applications that can be built, but it also creates the possibility that malicious or inefficient code can clog up the network, potentially leading to denial-of-service attacks, network spam, and other problems.

### Preventing Infinite Loops

Gas to the rescue! To prevent accidental or intentional infinite loops in smart contract code, Ethereum requires that every transaction specify a gas limit. The gas limit establishes the maximum amount of gas that the transaction can consume, and they ensure that transactions are executed within a predetermined amount of computational resources, preventing the execution of code that might consume too much computation power and potentially cause the network to freeze or crash. Without gas, Ethereum's Turing completeness would be insecure and inefficient.

### Autonomous Execution

It's also important to note that gas enables the execution of smart contracts without the need for a central authority to monitor their execution. The gas system provides a mechanism for regulating the resources required to execute the code of these contracts as well. In other words, without gas, it would be difficult to guarantee that smart contracts could operate autonomously, fairly and efficiently.

---

## How does gas work?

### Ethereum Denominations

Before diving into the inner workings of gas, it's important to understand a few of the most common denominations used in Ethereum.

#### Ether (ETH)

Ether is the native cryptocurrency of the Ethereum network. Gas fees are paid in ETH.

#### Wei

Wei is the smallest denomination of Ethereum and is equivalent to 10^-18 ETH. It is used to represent very small amounts of ETH, usually gas prices and transaction fees. To put 10^-18 into perspective:

- 1 ETH = 1,000,000,000,000,000,000 wei
- 1 wei = 0.000000000000000001 ETH

#### Gwei

Gwei is commonly used to express the price of gas. One gwei is equivalent to one billionth of one ETH or 10^-9 ETH.

- 1 ETH = 1,000,000,000 gwei
- 1 gwei = 0.000000001 ETH

### Gas Price

Gas price on the network is denominated in gwei, and the gas fee is calculated as the product of the gas price and the amount of gas required for an operation. For example, if the gas price is 50 gwei, and an operation requires 100,000 units of gas, the gas fee would be 0.005 ETH (50 gwei x 100,000 gas = 0.005 ETH).

### Gas Limit

Gas limit is an essential component of the gas system in Ethereum. It defines the maximum amount of gas a user is willing to spend for a transaction to be processed. This gas limit is set by the sender of the transaction and represents the upper limit of computational resources that the transaction can consume. The Ethereum Virtual Machine (EVM) starts deducting the amount of gas used from the gas limit as soon as it starts processing the transaction.

Consider Alice wants to send some ETH to Bob. Alice specifies a gas limit of 100,000 units and a gas price of 10 gwei (0.00000001 ETH) per unit of gas. So, she's willing to spend a maximum of 0.001 ETH for this transaction (1,000,000 gwei).

The EVM, upon receiving Alice's transaction, starts executing it. As the transaction is processed, the EVM deducts the used gas from the gas limit. If the transaction completes before reaching the gas limit, the remaining unused gas is refunded to Alice's account.

Let's illustrate this with a couple scenarios:

- Suppose the transaction used 80,000 units of gas, leaving 20,000 units unused. Since the gas price was set at 10 gwei per unit, Alice would receive a refund of 0.0002 ETH (200,000 gwei) for the unused gas.

- In a different scenario, suppose Alice sends a transaction with a gas limit of 100,000 units. After processing all the opcodes in the transaction except for the last one, Alice's transaction has consumed 99,998 units of gas. The EVM checks and sees that the last opcode will initiate because there are 2 units of gas remaining, enough to start it. However, as the opcode executes, it becomes clear that it actually requires more than 2 units of gas. At this point, the EVM throws an "Out of Gas" exception and halts the transaction. In this scenario, Alice loses all 100,000 units of gas, as they are consumed in the attempted execution. All state changes that might have occurred during the execution are rolled back, and the ETH Alice tried to send to Bob is returned to her.

### Gas Estimation

Gas estimation is another key concept to understand. It refers to the process of predicting the amount of gas that will be required to execute a transaction. This is important because as we've seen in our example, the gas limit of a transaction needs to be set before it can be broadcasted to the network. If the gas limit is set too low, the transaction may fail to execute, while if it is set too high, the sender may end up paying more in transaction fees than is necessary.

There are several methods that can be used for gas estimation. One common method is to use historical gas prices and gas limits as a reference point, and to estimate the gas needed for a new transaction based on the gas used in similar past transactions. Another method is to simulate the execution of the transaction in a test environment to determine the actual amount of gas that would be used.

Thankfully, most Ethereum wallet applications have built-in gas estimation algorithms that can automatically calculate an appropriate gas limit for a transaction based on the network conditions at the time the transaction is initiated. This helps to prevent a transaction from failing from the gas limit being too low while optimizing for the best possible cost for the sender.

---

## Conclusion

Gas is a vital component of Ethereum. It's what regulates the execution of all transactions and smart contracts, and it plays a significant role in the proper functioning and security of the network. Without gas, Ethereum's Turing-complete architecture would be inefficient and vulnerable to attacks. Gas also ensures that smart contracts can operate autonomously, fairly, and efficiently without the need for a central authority to monitor their execution. Understanding how gas works is essential for anyone who wants to develop applications or smart contracts on the Ethereum network.

---

## See also

- [Gas and Fees (Ethereum Docs)](https://ethereum.org/en/developers/docs/gas/)
- [Transaction Gas (Mastering Ethereum)](https://github.com/ethereumbook/ethereumbook/blob/develop/06transactions.asciidoc#transaction-gas)
- [Turing Completeness and Gas (Mastering Ethereum)](https://github.com/ethereumbook/ethereumbook/blob/develop/13evm.asciidoc#turing-completeness-and-gas)
- [Gas (Mastering Ethereum)](https://github.com/ethereumbook/ethereumbook/blob/develop/13evm.asciidoc#gas)

<!-- Reference Style Links -->

[Ethereum Docs]: https://ethereum.org/en/developers/docs/
[Mastering Ethereum]: https://github.com/ethereumbook/ethereumbook
[Ethereum demonimations]: https://www.gemini.com/en-US/cryptopedia/satoshi-value-gwei-to-ether-to-wei-converter-eth-gwei



<!-- File: ../web/apps/base-docs/base-learn/docs/minimal-tokens/minimal-tokens-exercise.md -->

---
title: Minimal Tokens Exercise
description: Exercise - Create your own token!
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a contract called `UnburnableToken`. Add the following in storage:

- A public mapping called `balances` to store how many tokens are owned by each address
- A `public uint` to hold `totalSupply`
- A `public uint` to hold `totalClaimed`
- Other variables as necessary to complete the task

Add the following functions.

### Constructor

Add a constructor that sets the total supply of tokens to 100,000,000.

### Claim

Add a `public` function called `claim`. When called, so long as a number of tokens equalling the `totalSupply` have not yet been distributed, any wallet _that has not made a claim previously_ should be able to claim 1000 tokens. If a wallet tries to claim a second time, it should revert with `TokensClaimed`.

The `totalClaimed` should be incremented by the claim amount.

Once all tokens have been claimed, this function should revert with an error `AllTokensClaimed`. (We won't be able to test this, but you'll know if it's there!)

### Safe Transfer

Implement a `public` function called `safeTransfer` that accepts an address `_to` and an `_amount`. It should transfer tokens from the sender to the `_to` address, **only if**:

- That address is not the zero address
- That address has a balance of greater than zero Base Sepolia Eth

A failure of either of these checks should result in a revert with an `UnsafeTransfer` error, containing the address.

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

:::caution

The contract specification contains actions that can only be performed once by a given address. As a result, the unit tests for a passing contract will only be successful the **first** time you test.

**You may need to submit a fresh deployment to pass**

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={13}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/minimal-tokens/creating-a-minimal-token-vid.md -->

---
title: Create a Minimal Token
description: Learn to build a very simple token.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035821' title='Creating a Minimal Token' />



<!-- File: ../web/apps/base-docs/base-learn/docs/minimal-tokens/minimal-token-sbs.md -->

---
title: Minimal Token
description: Build your own minimal token.
hide_table_of_contents: false
---

At their core, tokens are very simple. The technology powering famous NFT collections and fungible tokens worth vast amounts of money simply uses the EVM to keep track of who owns what, and provides a permissionless way for the owner to transfer what they own to someone new.

---

## Objectives

By the end of this lesson you should be able to:

- Construct a minimal token and deploy to testnet
- Identify the properties that make a token a token

---

## Implementing a Token

The minimal elements needed for a token are pretty basic. Start by creating a contract called `MinimalToken`. Add a `mapping` to relate user addresses to the number of tokens they possess. Finally, add a variable to track `totalSupply`:

<details>

<summary>Reveal code</summary>

```solidity
contract MinimalToken {
    mapping (address => uint) public balances;
    uint public totalSupply;
}
```

</details>

<br/>

Add a `constructor` that initializes the `totalSupply` at 3000 and assigns ownership to the contract creator:

<details>

<summary>Reveal code</summary>

```solidity
constructor() {
    totalSupply = 3000;

    balances[msg.sender] = totalSupply;
}
```

</details>

<br/>

Deploy and test to confirm that the total supply is 3000, and the balance of the first account is as well.

![Balance](../../assets/images/minimal-tokens/balance.png)

Update the constructor and hardcode a distribution of the tokens to be evenly split between the first three test accounts:

<details>

<summary>Reveal code</summary>

```solidity
constructor() {
    totalSupply = 3000;

    balances[msg.sender] = totalSupply / 3;
    balances[0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2] = totalSupply / 3;
    balances[0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db] = totalSupply / 3;
}
```

</details>

<br/>

Redeploy and test again. Now, each of the first three accounts should have 1000 tokens.

![Balance](../../assets/images/minimal-tokens/split-balances.png)

---

## Transferring Tokens

We can set an initial distribution of tokens and we can see balances, but we're still missing a way to allow the owners of these tokens to share them or spend them.

To remediate this, all we need to do is add a function that can update the balances of each party in the transfer.

Add a `function` called `transfer` that accepts an `address` of `_to` and a `uint` for the `_amount`. You don't need to add anything for `_from`, because that should only be `msg.sender`. The function should subtract the `_amount` from the `msg.sender` and add it to `_to`:

<details>

<summary>Reveal code</summary>

```solidity
function transfer(address _to, uint _amount) public {
    balances[msg.sender] -= _amount;
    balances[_to] += _amount;
}
```

</details>

<br/>

Double-check that you've switched back to the first address and redeploy. Then, try sending 500 tokens to the second address.

![Balance](../../assets/images/minimal-tokens/transferred.png)

What happens if you try to transfer more tokens than an account has? Give it a try!

```text
transact to MinimalToken.transfer pending ...
transact to MinimalToken.transfer errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Note: The called function should be payable if you send value and the value you send should be less than your current balance.
Debug the transaction to get more information.
```

You won't be able to do it, though the `Note:` here is **misleading**. In the EVM, `payable` **only** refers to transfers of the primary token used to pay gas fees: ETH, Base ETH, Sepolia ETH, Matic, etc. It does **not** refer to the balance of our simple token.

Instead, the transaction is reverting because of the built-in overflow/underflow protection. It's not a great programming practice to depend on this, so add an error for `InsufficientTokens` that returns the `newSenderBalance`.

```Solidity
function transfer(address _to, uint _amount) public {
    int newSenderBalance = int(balances[msg.sender] - _amount);
    if (newSenderBalance < 0) {
        revert InsufficientTokens(newSenderBalance);
    }

    balances[msg.sender] = uint(newSenderBalance);
    balances[_to] += _amount;
}
```

Try spending too much again. You'll get the same error in Remix:

```text
transact to MinimalToken.transfer pending ...
transact to MinimalToken.transfer errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Note: The called function should be payable if you send value and the value you send should be less than your current balance.
Debug the transaction to get more information.
```

However, you can use the debug tool to review the error in memory to see that it now matches your custom `error`.

## Destroying Tokens

Tokens can be effectively destroyed by accident, or on purpose. Accidental destruction happens when someone sends a token to an unowned wallet address. While it's possible that some day, some lucky person will create a new wallet and find a pleasant surprise, the most likely outcome is that any given randomly chosen address will never be used, thus no one will ever have the ability to use or transfer those tokens.

Luckily, there are some protections here. Similar to credit card numbers, addresses have a built-in checksum that helps protect against typos. Try it out by trying to transfer tokens to the second Remix address, but change the first character in the address from `A` to `B`. You'll get an error:

```text
transact to MinimalToken.transfer errored: Error encoding arguments: Error: bad address checksum (argument="address", value="0xBb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", code=INVALID_ARGUMENT, version=address/5.5.0) (argument=null, value="0xBb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", code=INVALID_ARGUMENT, version=abi/5.5.0)
```

A more guaranteed way to destroy, or _burn_ a token, is to transfer it to the default address `0x0000000000000000000000000000000000000000`. This address is unowned and unownable, making it mathematically impossible to retrieve any tokens that are sent to it. Redeploy and try it out by sending 1000 tokens to the zero address.

The `totalSupply` remains unchanged, and the balance of the zero address are visible, but those tokens are stuck there forever.

:::info

The [zero address] currently has a balance of more than 11,000 ETH, worth over **20 million dollars**! Its total holding of burned assets is estimated to be worth more than **200 million dollars**!!!

:::

---

## Conclusion

In this lesson, you've learned to implement a simple token, which is really just a system to store the balance of each address, and a mechanism to transfer them from one wallet to another. You've also learned how to permanently destroy tokens, whether by accident, or on purpose.

---

[zero address]: https://etherscan.io/address/0x0000000000000000000000000000000000000000



<!-- File: ../web/apps/base-docs/base-learn/docs/minimal-tokens/transferring-a-minimal-token-vid.md -->

---
title: Transferring a Minimal Token
description: Explore how tokens are given from one owner to another.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805238335' title='Transferring a Minimal Token' />



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/arrays-in-solidity-vid.md -->

---
title: Arrays
description: Learn about the unique properties of arrays in Solidity.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='827438004' title='Arrays in Solidity' />



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/filtering-an-array-sbs.md -->

---
title: Filtering an Array
description: Explore techniques to filter an array.
hide_table_of_contents: false
---

In this exercise, you'll explore two different solutions for filtering an array in Solidity. By doing so, you'll gain a better understanding of the constraints present while working with arrays, and have the chance to learn and compare the gas costs of different approaches.

---

## Objectives

By the end of this lesson you should be able to:

- Write a function that can return a filtered subset of an array

---

## First Pass Solution

### Setup

Create a new workspace in Remix and add a file called `ArrayDemo.sol` containing a `contract` called `ArrayDemo`. Initialize an array containing the numbers from 1 to 10. Add a stub for a function called `getEvenNumbers` that returns a `uint[] memory`.

```solidity
contract ArrayDemo {
    uint[] public numbers = [1,2,3,4,5,6,7,8,9,10];

    function getEvenNumbers() external view returns(uint[] memory) {
        // TODO
    }
}
```

:::caution

You don't have to declare the size of the memory array to be returned. You usually don't want to either, unless the results will always be the same, known size.

:::

### Finding the Number of Even Numbers

We need to initialize a `memory` array to hold the results, but to do so, we need to know how big to make the array. Don't be tempted to count the number of evens in `numbers`, as what happens if we modify it later?

The simple and obvious solution is to simply iterate through `numbers` and count how many even numbers are present. You could add that functionality in `getEvenNumbers()`, but it might be useful elsewhere, so a better practice would be to separate these concerns into another function.

Go ahead and write it on your own. It needs to:

- Instantiate a `uint` to hold the results
- Iterate through all values in `numbers` and increment that number if the value is even
- Return the result

You should end up with something like:

<details>

<summary>Reveal code</summary>

```solidity
function _countEvenNumbers() internal view returns(uint) {
    uint result = 0;

    for(uint i = 0; i < numbers.length; i++) {
        if(numbers[i] % 2 == 0) {
            result++;
        }
    }

    return result;
}
```

</details>

<br/>

The `_` in front of the function name is a practice used by some developers, in Solidity and in other languages, to indicate visually that this function is intended for internal use only.

### Returning Only Even Numbers

Now that we have a method to find out how big the return array needs to be in `getEvenNumbers()`, we can simply loop through `numbers`, and add the even numbers to the array to be returned.

Finish the function on your own. It needs to:

- Determine the number of results and instantiate an array that size
- Loop through the `numbers` array and if a given number is even, add it to the next unused index in the results array

You should end up with something like:

<details>

<summary>Reveal code</summary>

```solidity

function getEvenNumbers() external view returns(uint[] memory) {
    uint resultsLength = _countEvenNumbers();
    uint[] memory results = new uint[](resultsLength);
    uint cursor = 0;

    for(uint i = 0; i < numbers.length; i++) {
        if(numbers[i] % 2 == 0) {
            results[cursor] = numbers[i];
            cursor++;
        }
    }

    return results;
}

```

</details>

<br/>

Did you catch the compiler warning about `view`? You aren't modifying state, so you should mark it as such.

### Testing the Function

Deploy your contract and test the function. You should get a return of `[2,4,6,8,10]`. The total gas cost will be about 63,947, depending on if you used the same helper variables, etc.

---

## Optimizing the Function

It does seem inefficient to loop through the same array twice. What if we instead kept track of how many even numbers to expect. That way, we would only need to loop once, thus saving gas! Right?

Only one way to find out.

### Tracking Relevant Data

Add a contract-level variable called `numEven`, and initialize it with **5**, the number of even numbers in the array. Modify `getEvenNumbers()` to use `numEven` instead of the `_countEvenNumbers()` function. It should now look like:

<details>

<summary>Reveal code</summary>

```solidity
function getEvenNumbers() external view returns(uint[] memory) {
    uint resultsLength = numEven; // <- Changed here
    uint[] memory results = new uint[](resultsLength);
    uint cursor = 0;

    for(uint i = 0; i < numbers.length; i++) {
        if(numbers[i] % 2 == 0) {
            results[cursor] = numbers[i];
            cursor++;
        }
    }

    return results;
}
```

</details>

<br/>

Redeploy and test again. Success, the function now only costs about 57,484 gas to run! Except there is a catch. Remember, it's going to cost about 5000 gas to update `numEven` **each time** the array adds an even number.

### A More Realistic Accounting

As we considered above, in a real-world example, we wouldn't declare the array up front, it would be modified over time. A slightly more realistic example would be to fill the array with a function.

Change the declaration for `numbers` and `numEven` so that they have their respective default values to begin with.

```solidity
uint[] public numbers;
uint numEven;
```

Add a new function called `debugLoadArray` that takes a `uint` called `_number` as an argument, and fills the array by looping through `_number` times, pushing each number into the array. **For now, _don't_ update `numEven`**.

<details>

<summary>Reveal code</summary>

```solidity
function debugLoadArray(uint _number) external {
    for(uint i = 0; i < _number; i++) {
        numbers.push(i);
    }
}
```

</details>

<br/>

Test out the function by loading in **10** numbers. It costs about 249,610 gas to load the array. Now, add functionality to **also** increment `numEven` when the number added is even. We can't just calculate it, because although the numbers are sequential in the debug function, they might not be in real world use.

<details>

<summary>Reveal code</summary>

```solidity
function debugLoadArray(uint _number) external {
    for(uint i = 0; i < _number; i++) {
        numbers.push(i);
        if(i % 2 == 0) {
            numEven++;
        }
    }
}
```

</details>

<br/>

**Be sure to redeploy** and try again with **10** numbers. This time, the cost was about 275,335 gas. That's almost 26,000 more gas in an effort to save the 5,000 gas needed to run `_countEvenNumbers()`.

### Looking at the Big Picture

What about more? What if there are a thousand numbers in the array? What about a million?

Let's start with 500, any more will break the Remix EVM simulation, and/or would trigger an out of gas error because we're approaching the gas limit for the entire block.

**Comment out** the `if` statement in `debugLoadArray` that checks for even numbers and load 500 numbers. The Remix EVM should be able to handle this, but it might hang up for a moment, or even crash. (You can also do this experiment with 250 numbers instead.)

```solidity
function debugLoadArray(uint _number) external {
    for(uint i = 0; i < _number; i++) {
        numbers.push(i);
        // if(i % 2 == 0) {
        //    numEven++;
        //}
    }
}
```

You'll get a result of about 11,323,132 gas to load the array. That's a lot! The target total gas for a single block is 15 million, and the limit is 30 million.

Try again with the code to increment `numEven`. You should get about 11,536,282, or an increase of about 213,150 gas.

Now, test out `getEvenNumbers()` using `numEven` vs. using `_countEvenNumbers()`. With `numEven`, it should cost about 1,578,741 gas to find the even numbers. Using `_countEvenNumbers()`, that cost increases to 1,995,579 gas, an increase of 416,838 gas.

### Which is Better?

As is often the case with code, it depends. You might think that the experiment makes things obvious. Paying 213k gas up front to track `_numEven` results in a savings of over 400k gas when filtering for even numbers. Even better, you might realize that the upfront cost difference will be spread across all of your users over time, making them almost trivial. You also might think that it's possible that the filter function could be called dozens of times for each time 500 numbers are loaded.

These are all valid considerations that you should evaluate as you are developing your code solution to a business problem. One last critical element to consider is that there is only a gas cost to read from the blockchain if it's another contract calling the function. It **doesn't** cost any gas to call `view` or `pure` functions from a front end or app.

If `getEvenNumbers` will never be called by another contract, then using `numEven` might cost more for no benefit!

---

## Conclusion

In this lesson, you've explored a few different approaches to a problem. You've learned how to filter an array, but more importantly, you've learned some of the specific considerations in blockchain development. Finally, you've seen that pushing 500 integers to an array, usually a trivial operation, is very large and very expensive on the EVM.



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/arrays-in-solidity.md -->

---
title: Arrays
description: An overview of how arrays work in Solidity.
hide_table_of_contents: false
---

Solidity arrays are collections of the same type, accessed via an index, the same as any other language. Unlike other languages, there are three types of arrays - _storage_, _memory_, and _calldata_. Each has their own properties and constraints.

---

## Objectives

By the end of this lesson you should be able to:

- Describe the difference between storage, memory, and calldata arrays

---

## Storage, Memory, and Calldata

The `storage`, `memory`, or `calldata` keywords are required when declaring a new [reference type] variable. This keyword determines the [data location] where the variable is stored and how long it will persist.

### Storage

The `storage` keyword is used to assign state variables that become a part of the blockchain as a part of the _storage_ for your contract. These remain as assigned until modified, for the lifetime of the contract.

Storage is **very expensive** compared to most other environments. It costs a minimum of 20000 gas to [store a value] in a new storage slot, though it's cheaper to update that value after the initial assignment (~5000+ gas).

This cost isn't a reason to be afraid of using storage. In the long run, writing clear, maintainable, and logical code will always cost less than jumping through hoops to save gas here and there. Just be as thoughtful with storage on the EVM as you would be with computation in most other environments.

### Memory

The `memory` keyword creates temporary variables that only exist within the scope in which they are created. Memory is less expensive than storage, although this is relative. There are often circumstances where it is cheaper to work directly in storage rather than convert to memory and back. Copying from one location to another can be quite expensive!

### Calldata

The `calldata` storage location is where function arguments are stored. It is non-modifiable and the Solidity docs recommend using it where possible to avoid unnecessary copying, because it can't be modified. You'll learn more about this later, but doing so can help prevent confusing bugs when calling a function from another contract that takes in values from that contract's `storage`.

---

## Array Data Locations

Arrays behave differently based on their data location. Assignment behavior also depends on data location. To [quote the docs]:

> - Assignments between `storage` and `memory` (or from `calldata`) always create an independent copy.
>
> - Assignments from `memory` to `memory` only create references. This means that changes to one memory variable are also visible in all other memory variables that refer to the same data.
>
> - Assignments from `storage` to a **local** storage variable also only assign a reference.
>
> - All other assignments to `storage` always copy. Examples for this case are assignments to state variables or to members of local variables of storage struct type, even if the local variable itself is just a reference.

### Storage Arrays

_Arrays_ in `storage` are passed by _reference_. In other words, if you assign a _storage array_ half a dozen names, any changes you make will always modify the original, underlying storage array.

```solidity
contract StorageArray {
    // Variables declared at the class level are always `storage`
    uint[] arr = [1, 2, 3, 4, 5];

    function function_1() public {
        uint[] storage arr2 = arr;

        arr2[0] = 99; // <- arr is now [99, 2, 3, 4, 5];
    }
}
```

You cannot use a `storage` array as a function parameter, and you cannot write a function that `return`s a `storage` array.

Storage arrays are dynamic, unless they are declared with an explicit size. However, their functionality is limited compared to other languages. The `.push(value)` function works as expected. The `.pop()` function removes the last value of an array, but it **does not** return that value. You also **may not** use `.pop()` with an index to remove an element from the middle of an array, or to remove more than one element.

You can use the `delete` keyword with an array. Doing so on an entire array will reset the array to zero length. Calling it on an element within the array will reset that value to its default. It **will not** resize the array!

```solidity
uint[] arr_2 = [1, 2, 3, 4, 5];
function function_2(uint _num) public returns(uint[] memory) {
    arr_2.push(_num); // <- arr_2 is [1, 2, 3, 4, 5, <_num>]

    delete arr_2[2];  // <- arr_2 is [1, 2, 0, 4, 5, <_num>]

    arr_2.pop();  // <- arr_2 is [1, 2, 0, 4, 5] (_num IS NOT returned by .pop())

    delete arr_2; // <- arr_2 is []

    return arr_2; // <- returns []
}
```

Storage arrays are implicitly convertible to `memory` arrays.

### Memory Arrays

Arrays declared as `memory` are temporary and only exist within the scope in which they are created. Arrays in `memory` are **not** dynamic and must be declared with a fixed size. This can be done at compile time, by declaring a size inside the `[]` or during runtime by using the `new` keyword. Finally, `memory` arrays can be implicitly cast from `storage` arrays.

```solidity
function function_3(uint _arrSize) public {
    uint[5] memory arrSizeFive;
    uint[] memory arrWithCustomSize = new uint[](_arrSize);
    uint[] memory localCopyOfArr = arr;
    // ...do something
}
```

The declaration pattern impacts gas cost, though keep in mind that the first two examples are empty, and would cost additional gas depending on how they are eventually filled.

```solidity
function declareMemoryArrays() public view {
    uint[5] memory simpleArr; // this line costs 135 gas
    uint[] memory emptyArr = new uint[](5); // This line costs 194 gas
    uint[] memory arrCopy = arr; // This line costs 13166 gas
}
```

The lack of dynamic `memory` arrays can require some gymnastics if you need to create an array where the size is not initially known. Depending on the specific needs of the problem, valid solutions for filtering an array and returning a smaller array could include:

- Looping through a larger array twice, first to count the number, then to copy the appropriate elements
- Tracking the number of elements that meet condition X with a storage variable, then instantiating the array with `<type>[] memory filteredArray = new <type>[](numX);`
- Using multiple data structures to track references to different subsets

### Calldata Arrays

Arrays in `calldata` are read only. Otherwise, they function the same as any other array.

Array [slices] are currently only implemented for `calldata` arrays.

---

## Conclusion

In this lesson, you've learned the differences between the `memory`, `storage`, and `calldata` data locations. You've also learned how they apply to arrays, with each having its own properties, restrictions, and costs.

---

<!-- Reference Style Links -->

[data location]: https://docs.soliditylang.org/en/v0.8.17/types.html?highlight=calldata#data-location
[reference type]: https://docs.soliditylang.org/en/v0.8.17/types.html?highlight=array#reference-types
[store a value]: https://github.com/wolflo/evm-opcodes/blob/main/gas.md#a7-sstore
[quote the docs]: https://docs.soliditylang.org/en/v0.8.17/types.html?#data-location-and-assignment-behaviour
[slices]: https://docs.soliditylang.org/en/v0.8.17/types.html?#array-slices



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/fixed-size-arrays-vid.md -->

---
title: Fixed-Size Arrays
description: Learn about fixed-size arrays.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='806136952' title='Fixed-Size Arrays' />



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/writing-arrays-in-solidity-vid.md -->

---
title: Writing Arrays
description: Learn how to write arrays in Solidity.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='806137037' title='Writing Arrays in Solidity' />



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/arrays-exercise.md -->

---
title: Arrays Exercise
description: Exercise - Demonstrate your knowledge of arrays.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Review the contract in the starter snippet called `ArraysExercise`. It contains an array called `numbers` that is initialized with the numbers 1–10. Copy and paste this into your file.

```solidity
contract ArraysExercise {
    uint[] public numbers = [1,2,3,4,5,6,7,8,9,10];
}
```

Add the following functions:

### Return a Complete Array

The compiler automatically adds a getter for individual elements in the array, but it does not automatically provide functionality to retrieve the entire array.

Write a function called `getNumbers` that returns the entire `numbers` array.

### Reset Numbers

Write a `public` function called `resetNumbers` that resets the `numbers` array to its initial value, holding the numbers from 1-10.

:::note

We'll award the pin for any solution that works, but one that **doesn't** use `.push()` is more gas-efficient!

:::

:::caution

Remember, _anyone_ can call a `public` function! You'll learn how to protect functionality in another lesson.

:::

### Append to an Existing Array

Write a function called `appendToNumbers` that takes a `uint[] calldata` array called `_toAppend`, and adds that array to the `storage` array called `numbers`, already present in the starter.

### Timestamp Saving

At the contract level, add an `address` array called `senders` and a `uint` array called `timestamps`.

Write a function called `saveTimestamp` that takes a `uint` called `_unixTimestamp` as an argument. When called, it should add the address of the caller to the end of `senders` and the `_unixTimeStamp` to `timestamps`.

:::tip

You'll need to research on your own to discover the correct _Special Variables and Functions_ that can help you with this challenge!

:::

### Timestamp Filtering

Write a function called `afterY2K` that takes no arguments. When called, it should return two arrays.

The first should return all timestamps that are more recent than January 1, 2000, 12:00am. To save you a click, the Unix timestamp for this date and time is `946702800`.

The second should return a list of `senders` addresses corresponding to those timestamps.

### Resets

Add `public` functions called `resetSenders` and `resetTimestamps` that reset those storage variables.

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={4}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/arrays/array-storage-layout-vid.md -->

---
title: Array Storage Layout
description: Learn how arrays are kept in storage.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='806136995' title='Array Storage Layout' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-verify/hardhat-verify-vid.md -->

---
title: Verifying Smart Contracts
description: Verify your contracts with Hardhat.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='844046789' title='Verifying Smart Contracts' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-verify/hardhat-verify-sbs.md -->

---
title: Verifying Smart Contracts
description: Verifying smart contracts with Hardhat.
hide_table_of_contents: false
---

In this article, you'll learn how to verify smart contracts in Etherscan with hardhat and the hardhat deploy plugin.

---

## Objectives

By the end of this lesson, you should be able to:

- Verify a deployed smart contract on Etherscan
- Connect a wallet to a contract in Etherscan
- Use etherscan to interact with your own deployed contract

---

## Overview

Verifying smart contracts plays an important role in providing security and certainty to the users of your decentralized applications. By offering full visibility of the source code of your smart contract, you provide confidence and transparency of the intention of the code that is being executed.

The way smart contracts are verified is by simply uploading the source code and contract address to services such as Etherscan.

Once the contract is verified, the Etherscan explorer shows a status like the following image:

![Verified contract](../../assets/images/hardhat-verify/hardhat-verify.png)

Luckily, Hardhat and Hardhat-deploy already contain a built-in capability to do this task easily on your behalf.

This process involves the following steps:

1. Getting an Etherscan key
2. Configuring Hardhat
3. Verifying

## Getting an Etherscan key

In order to obtain an Etherscan API key, visit [Etherscan](https://etherscan.io/) and create an account.

Then, go to [https://etherscan.io/myapikey](https://etherscan.io/myapikey) and create an API key by clicking the **Add** button:

![Add key](../../assets/images/hardhat-verify/harhat-verify-create-key.png)

Bear in mind that different networks have other Blockchain explorers. For example:

- [Base](https://basescan.org/)
- [Sepolia](https://sepolia.etherscan.io/)

You'll need to go to that particular explorer and get the API Key following a similar process as mentioned previously (except for Sepolia Etherscan, where you can use the Etherscan mainnet one instead).

## Configuring Hardhat

You can configure the Etherscan API Key for each different network. For example, include the following to the `hardhat.config.ts` file for Base Sepolia:

```tsx
base_sepolia: {
  url: "https://sepolia.base.org",
  accounts: {
    mnemonic: process.env.MNEMONIC ?? ""
  },
  verify: {
    etherscan: {
      apiUrl: "https://api-sepolia.basescan.org",
      apiKey: process.env.ETHERSCAN_API_KEY
    }
  }
}
```

Include in your `.env` file the following:

```
ETHERSCAN_API_KEY=<YOUR_ETHERSCAN_API_KEY>
```

## Verifying

You verify in base, and to do so, simply run the following command:

```bash
npx hardhat --network base_sepolia etherscan-verify
```

You should receive the following response:

```
verifying Lock ...
waiting for result...
 => contract Lock is now verified
```

You can now go to Basescan and search for your contract address, where you'll see the following:

![Base scan success](../../assets/images/hardhat-verify/hardhat-verify-success.png)

## Conclusion

In this lesson, you've learned how to verify smart contracts using Hardhat and Hardhat-deploy. You learned how to configure Hardhat to support multiple networks and verify by using a simple command.

---

## See also

[Solidity Docs]: https://docs.soliditylang.org/en/v0.8.17/
[Remix Project]: https://remix-project.org/
[Hardhat Deploy]: https://github.com/wighawag/hardhat-deploy



<!-- File: ../web/apps/base-docs/base-learn/docs/mappings/mappings-exercise.md -->

---
title: Mappings Exercise
description: Exercise - Demonstrate your knowledge of mappings.
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a single contract called `FavoriteRecords`. It should not inherit from any other contracts. It should have the following properties:

### State Variables

The contract should have the following state variables. It is **up to you** to decide if any supporting variables are useful.

- A public mapping `approvedRecords`, which returns `true` if an album name has been added as described below, and `false` if it has not
- A mapping called `userFavorites` that indexes user addresses to a mapping of `string` record names which returns `true` or `false`, depending if the user has marked that album as a favorite

### Loading Approved Albums

Using the method of your choice, load `approvedRecords` with the following:

- Thriller
- Back in Black
- The Bodyguard
- The Dark Side of the Moon
- Their Greatest Hits (1971-1975)
- Hotel California
- Come On Over
- Rumours
- Saturday Night Fever

### Get Approved Records

Add a function called `getApprovedRecords`. This function should return a list of all of the names currently indexed in `approvedRecords`.

### Add Record to Favorites

Create a function called `addRecord` that accepts an album name as a parameter. **If** the album is on the approved list, add it to the list under the address of the sender. Otherwise, reject it with a custom error of `NotApproved` with the submitted name as an argument.

### Users' Lists

Write a function called `getUserFavorites` that retrieves the list of favorites for a provided `address memory`.

### Reset My Favorites

Add a function called `resetUserFavorites` that resets `userFavorites` for the sender.

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={5} />



<!-- File: ../web/apps/base-docs/base-learn/docs/mappings/how-mappings-are-stored-vid.md -->

---
title: How Mappings are Stored
description: Learn about `msg.sender`.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479611' title='How Mappings are Stored' />



<!-- File: ../web/apps/base-docs/base-learn/docs/mappings/using-msg-sender-vid.md -->

---
title: Using `msg.sender`
description: Learn about `msg.sender`.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479641' title='Using `msg.sender`' />



<!-- File: ../web/apps/base-docs/base-learn/docs/mappings/mappings-sbs.md -->

---
title: Mappings
description: Use the mapping data type to store key-value pairs.
hide_table_of_contents: false
---

In Solidity, the hashtable/hashmap/dictionary-comparable type used to store key-value pairs is called a `mapping`. `mapping`s are a powerful tool with many uses, but they also have some unexpected limitations. They also **aren't** actually hash tables!

---

## Objectives

By the end of this lesson you should be able to:

- Construct a Map (dictionary) data type
- Recall that assignment of the Map data type is not as flexible as for other data types/in other languages
- Restrict function calls with the `msg.sender` global variable
- Recall that there is no collision protection in the EVM and why this is (probably) ok

---

## Mappings in Solidity vs. Hash Tables

On the surface, the [`mapping`] data type appears to be just another hash table implementation that stores pairs of any hashable type as a key, to any other type as a value. The difference is in implementation.

In a more traditional implementation, the data is stored in memory as an array, with a hash-to-index _(hashmod)_ function used to determine which spot in the array to store a given value, based on the key. Sometimes, the _hashmod_ function for two different keys results in the same index, causing a _collision_.

Collisions are resolved via additional solutions, such as linked list chaining; when the underlying array starts to get full, a bigger one is created, all the keys are re-hash-modded, and all the values moved over to the new array.

In the EVM, `mappings` do **not** have an array as the underlying data structure. Instead, the `keccak256` hash of the key plus the storage slot for the mapping itself is used to determine which storage slot out of all 2\*\*256 will be used for the value.

There is no collision-handling, for the same reason that makes wallets work at all - 2\*\*256 is an unimaginably large number. One of the biggest numbers you might encounter regularly is the number of possible configurations for a [shuffled deck of cards], which is:

80658175170943878571660636856403766975289505440883277824000000000000

Meanwhile, the number of variations of a `keccak256` hash are:

115792089237316195423570985008687907853269984665640564039457584007913129639935

Collisions are very unlikely.

As a result, there are a few special characteristics and limitations to keep in mind with the `mapping` data type:

- Mappings can only have a data location of `storage`
- They can't be used as parameters or returns of public functions
- They are not iterable and you cannot retrieve a list of keys
- All possible keys will return the default value, unless another value has been stored

### Creating a Mapping

Create a contract called `Mappings`. In it, add a `mapping` from an `address` to a `uint` called `favoriteNumbers`.

<details>

<summary>Reveal code</summary>

```solidity
contract Mappings {
    mapping (address => uint) favoriteNumbers;
}
```

</details>

<br/>

### Writing to the Mapping

Add a function called `saveFavoriteNumber` that takes an `address` and `uint`, then saves the `uint` in the mapping, with the `address` as the key.

<details>

<summary>Reveal code</summary>

```solidity
function saveFavoriteNumber(address _address, uint _favorite) public {
    favoriteNumbers[_address] = _favorite;
}
```

</details>

<br/>

Deploy and test it out. Does it work? Probably...

You don't have a way to read the data in `favoriteNumber`, but this problem is easy to correct. Similar to arrays, if you mark a `mapping` as public, the Solidity compiler will automatically create a getter for values in that `mapping`.

Update the declaration of `favoriteNumbers` and deploy to test again.

### Utilizing msg.sender

Another issue with this contract is that a `public` function can be called by anyone and everyone with a wallet and funds to pay gas fees. As a result, anyone could go in after you and change your favorite number from lucky number **13** to anything, even **7**!

That won't do at all!

Luckily, you can make use of a [global variable] called `msg.sender` to access the `address` of the wallet that sent the transaction. Use this to make it so that only the owner of an `address` can set their favorite number.

<details>

<summary>Reveal code</summary>

```solidity
function saveFavoriteNumber(uint _favorite) public {
    favoriteNumbers[msg.sender] = _favorite;
}
```

</details>

<br/>

Deploy and test again. Success!

---

## Retrieving All Favorite Numbers

One challenging limitation of the `mapping` data type is that it is **not** iterable - you cannot loop through and manipulate or return **all** values in the `mapping`.

At least not with any built-in features, but you can solve this on your own. A common practice in Solidity with this and similar problems is to use multiple variables or data types to store the right combination needed to address the issue.

### Using a Helper Array

For this problem, you can use a helper array to store a list of all the keys present in `favoriteNumbers`. Simply add the array, and push new keys to it when saving a new favorite number.

<details>

<summary>Reveal code</summary>

```solidity
contract Mappings {
    mapping (address => uint) public favoriteNumbers;
    address[] addressesOfFavs;

    function saveFavoriteNumber(uint _favorite) public {
        favoriteNumbers[msg.sender] = _favorite;
        // Imperfect solution, see below
        addressesOfFavs.push(msg.sender);
    }
}
```

</details>

<br/>

To return all of the favorite numbers, you can then iterate through `addressesOfFavs`, look up that addresses' favorite number, add it to a return array, and then return the array when you're done.


<details>

<summary>Reveal code</summary>

```solidity
function returnAllFavorites() public view returns (uint[] memory) {
    uint[] memory allFavorites = new uint[](addressesOfFavs.length);

    for(uint i = 0; i < allFavorites.length; i++) {
        allFavorites[i] = favoriteNumbers[addressesOfFavs[i]];
    }

    return allFavorites;
}
```

</details>

<br/>

On the surface, this solution works, but there is a problem: What happens if a user **updates** their favorite number? Their address will end up in the list twice, resulting in a doubled entry in the return.

A solution here would be to check first if the `address` already has a number as a value in `favoriteNumbers`, and only push it to the array if not.

<details>

<summary>Reveal code</summary>

```solidity
function saveFavoriteNumber(uint _favorite) public {
    if(favoriteNumbers[msg.sender] == 0) {
        addressesOfFavs.push(msg.sender);
    }
    favoriteNumbers[msg.sender] = _favorite;
}
```

</details>

<br/>

You should end up with a contract similar to this:

<details>

<summary>Reveal code</summary>

```solidity
pragma solidity 0.8.17;

contract Mappings {
    mapping (address => uint) public favoriteNumbers;
    address[] addressesOfFavs;

    function saveFavoriteNumber(uint _favorite) public {
        if(favoriteNumbers[msg.sender] == 0) {
            addressesOfFavs.push(msg.sender);
        }
        favoriteNumbers[msg.sender] = _favorite;
    }

    function returnAllFavorites() public view returns (uint[] memory) {
        uint[] memory allFavorites = new uint[](addressesOfFavs.length);

        for(uint i = 0; i < allFavorites.length; i++) {
            allFavorites[i] = favoriteNumbers[addressesOfFavs[i]];
        }

        return allFavorites;
    }
}
```

</details>

---

## Conclusion

In this lesson, you've learned how to use the `mapping` data type to store key-value pairs in Solidity. You've also explored one strategy for solving some of the limitations found in the `mapping` type when compared to similar types in other languages.

---

[`mapping`]: https://docs.soliditylang.org/en/v0.8.17/types.html#mapping-types
[hash table]: https://en.wikipedia.org/wiki/Hash_table
[shuffled deck of cards]: https://czep.net/weblog/52cards.html
[global variable]: https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html



<!-- File: ../web/apps/base-docs/base-learn/docs/mappings/mappings-vid.md -->

---
title: Mappings
description: Learn about mappings.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804479619' title='Mappings' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/deployment-vid.md -->

---
title: Deployment
description: Configure test networks.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='844046070' title='Deployment' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/installing-hardhat-deploy-vid.md -->

---
title: Installing Hardhat Deploy
description: Install a community plugin that makes deployments easier.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='841276722' title='Installing Hardhat Deploy' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/setup-deploy-script-vid.md -->

---
title: Setting up the Deploy Script
description: Prepare a script to deploy your contract.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='841279882' title='Setting up the Deploy Script' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/hardhat-deploy-sbs.md -->

---
title: Deploying Smart Contracts
description: Deploy smart contracts with hardhat deploy and hardhat
hide_table_of_contents: false
---

In this article, you'll learn how to deploy smart contracts to multiple Blockchain networks using Hardhat and Hardhat deploy.

---

## Objectives

By the end of this lesson, you should be able to:

- Deploy a smart contract to the Base Sepolia Testnet with hardhat-deploy
- Deploy a smart contract to the Sepolia Testnet with hardhat-deploy
- Use BaseScan to view a deployed smart contract

---

## Overview

Hardhat capabilities enable developers to deploy smart contracts easily to any Blockchain by simply creating `tasks` or `scripts`. However, due to the Hardhat architecture that enables its extension by creating plugins, you can rely on existing solutions developed by the community.

[Hardhat deploy](https://github.com/wighawag/hardhat-deploy) is a community-developed plugin that enables the deployment of your smart contracts in a simple way.

## Setting up Hardhat deploy

To install:

1. Run `npm install -D hardhat-deploy`. Then, import hardhat-deploy in `hardhat.config.ts`:

```tsx
import 'hardhat-deploy';
```

2. Create a folder called deploy and inside it create a new file called `001_deploy_lock.ts`.

3. Include the following:

```tsx
import { HardhatRuntimeEnvironment } from 'hardhat/types';
import { DeployFunction } from 'hardhat-deploy/types';

const func: DeployFunction = async function (hre: HardhatRuntimeEnvironment) {
  // code here
};
export default func;
```

4. Modify the `tsconfig.json` file to look like:

```json
{
  "compilerOptions": {
    "target": "es2020",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true,
    "resolveJsonModule": true
  },
  "include": ["./hardhat.config.ts", "./scripts", "./deploy", "./test"]
}
```

5. Before implementing the deploy functionality, configure a deployer account in the `hardhat.config.ts` file. Hardhat deployment includes a way to name accounts in the config file.

6. Run the following, which adds an alias to the account 0 of your environment:

```tsx
const config: HardhatUserConfig = {
  solidity: '0.8.23',
  namedAccounts: {
    deployer: 0,
  },
};
```

7. Implement the deploy function by including the following in the `001_deploy_lock.ts` file:

```tsx
import { HardhatRuntimeEnvironment } from 'hardhat/types';
import { DeployFunction } from 'hardhat-deploy/types';
import { ethers } from 'hardhat';

const func: DeployFunction = async function (hre: HardhatRuntimeEnvironment) {
  const { deploy } = hre.deployments;
  // We can now use deployer
  const { deployer } = await hre.getNamedAccounts();

  // The value we want to lock
  const VALUE_LOCKED = hre.ethers.parseEther('0.01');

  // The unlock time after deployment
  const UNLOCK_TIME = 10000;

  // We use ethers to get the current time stamp
  const blockNumber = await ethers.provider.getBlockNumber();
  const lastBlockTimeStamp = (await ethers.provider.getBlock(blockNumber))?.timestamp as number;

  // We say we want to deploy our Lock contract using the deployer
  // account and passing the value and arguments.
  await deploy('Lock', {
    from: deployer,
    args: [lastBlockTimeStamp + UNLOCK_TIME],
    value: VALUE_LOCKED.toString(),
  });
};

export default func;

// This tag will help us in the next section to trigger this deployment file programmatically
func.tags = ['DeployAll'];
```

## Testing your deployment

The easiest way to test your deployment is by modifying the test.

Go to `Lock.ts` and include in the imports the following:

```tsx
import { ethers, deployments } from 'hardhat';
```

`deployments` will allow you to execute the deployment files from your test.

Change the `before` function to look like the following:

```tsx
before(async () => {
  lastBlockTimeStamp = await time.latest();

  const signers = await ethers.getSigners();
  ownerSigner = signers[0];
  otherUserSigner = signers[1];

  await deployments.fixture(['DeployAll']);
  const lockDeployment = await deployments.get('Lock');

  lockInstance = Lock__factory.connect(lockDeployment.address, ownerSigner);
});
```

Notice how you execute `deployments.fixture` and pass a tag that matches the one you specified in the deployment file (`001_deploy_lock.ts`).

The deployment file is then executed and you can then reuse that functionality and simply consume the address of the newly-deployed contract by using:

```tsx
const lockDeployment = await deployments.get('Lock');
```

Reuse `Lock__factory` but use the connect function and pass the address of the newly-created contract plus a signer. Then, run `npx hardhat test` and you should get the same result:

```
  Lock
    ✔ should get the unlockTime value
    ✔ should have the right ether balance
    ✔ should have the right owner
    ✔ shouldn't allow to withdraw before unlock time (51ms)
    ✔ shouldn't allow to withdraw a non owner
    ✔ should allow to withdraw an owner

  6 passing (2s)
```

## Deploying to a test network

Deploying to a real test network involves configuring the network parameters in the hardhat config file. You need to include parameters such as:

- The JSON RPC URL
- The account you want to use
- Real test ether or the native Blockchain token for gas costs

Include the following in the `hardhat.config.ts` file:

```tsx
const config: HardhatUserConfig = {
  solidity: '0.8.18',
  namedAccounts: {
    deployer: 0,
  },
  networks: {
    base_sepolia: {
      url: 'https://sepolia.base.org',
      accounts: {
        mnemonic: process.env.MNEMONIC ?? '',
      },
    },
    sepolia: {
      url: `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_SEPOLIA_KEY ?? ''}`,
      accounts: {
        mnemonic: process.env.MNEMONIC ?? '',
      },
    },
  },
};
```

You've configured 2 networks:

- base_sepolia
- sepolia

You also need to create a `.env` file with the following variables:

```
MNEMONIC="<REPLACE WITH YOUR MNEMONIC>"
ALCHEMY_SEPOLIA_KEY=<REPLACE WITH YOUR API KEY>
```

In order to ensure the environment variables are loaded, you need to install another package called `dotenv`:

```bash
npm install -D dotenv
```

Then, include the following in the `hardhat.config.ts` file:

```tsx
import dotenv from 'dotenv';

dotenv.config();
```

Deploy to base with the following command:

```bash
npx hardhat deploy --network base_sepolia
```

After you run the command, a deployments folder appears with a newly-created deployment for `base_sepolia`:

![New deployment](../../assets/images/hardhat-deploying/new-deploy.png)

If you want to deploy to another network, change the network name as follows:

```bash
npx hardhat deploy --network sepolia
```

:::info

Be aware that you must have the correct environment variables for the JSON RPC URLs. For example, for Sepolia use `ALCHEMY_SEPOLIA_KEY`.

:::

## Conclusion

In this lesson, you've learned how to deploy smart contracts using Hardhat and Hardhat-deploy. You have configured hardhat to easily deploy to multiple networks and you created deployment files to abstract this task.

---

## See also

[Solidity Docs](https://docs.soliditylang.org/en/v0.8.17/)
[Remix Project]: https://remix-project.org/
[Hardhat]: https://hardhat.org/
[Hardhat Deploy]: https://github.com/wighawag/hardhat-deploy



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/test-network-configuration-vid.md -->

---
title: Test Network Configuration
description: Configure test networks.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='844045131' title='Test Network Configuration' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-deploy/testing-our-deployment-vid.md -->

---
title: Testing Our Deployment
description: Test the newly created deploy script.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='841281515' title='Testing Our Deployment' />



<!-- File: ../web/apps/base-docs/base-learn/docs/contracts-and-basic-functions/basic-functions-exercise.md -->

---
title: 'Basic Functions Exercise'
description: Exercise - Create and deploy a contract with simple math functions.
hide_table_of_contents: false
---

Each module in this course will contain exercises in which you are given a specification for a contract **without** being given specific instructions on how to build the contract. You must use what you've learned to figure out the best solution on your own!

:::info

Once you've learned how to deploy your contracts to a test network, you'll be given the opportunity to submit your contract address for review by an onchain unit test. If it passes, you'll receive an NFT pin recognizing your accomplishment.

**You'll deploy and submit this contract in the next module.**

:::

The following exercise asks you to create a contract that adheres to the following stated specifications.

## Contract

Create a contract called `BasicMath`. It should not inherit from any other contracts and does not need a constructor. It should have the following two functions:

### Adder

A function called `adder`. It must:

- Accept two `uint` arguments, called `_a` and `_b`
- Return a `uint` `sum` and a `bool` `error`
- If `_a` + `_b` does not overflow, it should return the `sum` and an `error` of `false`
- If `_a` + `_b` overflows, it should return `0` as the `sum`, and an `error` of `true`

### Subtractor

A function called `subtractor`. It must:

- Accept two `uint` arguments, called `_a` and `_b`
- Return a `uint` `difference` and a `bool` `error`
- If `_a` - `_b` does not underflow, it should return the `difference` and an `error` of `false`
- If `_a` - `_b` underflows, it should return `0` as the `difference`, and an `error` of `true`



<!-- File: ../web/apps/base-docs/base-learn/docs/contracts-and-basic-functions/basic-types.md -->

---
title: Basic Types
description: Introduction to basic types in Solidity.
hide_table_of_contents: false
---

Solidity contains most of the basic [types] you are used to from other languages, but their properties and usage are often a little different than other languages and are likely much more restrictive. In particular, Solidity is a very **explicit** language and will not allow you to make inferences most of the time.

---

## Objectives

By the end of this lesson you should be able to:

- Categorize basic data types
- List the major differences between data types in Solidity as compared to other languages
- Compare and contrast signed and unsigned integers

---

## Common Properties

In Solidity, [types] must always have a value and are never `undefined`, `null`, or `none`. Because of this, each type has a default value. If you declare a variable without assigning a value, it will instead have the default value for that type. This property can lead to some tricky bugs until you get used to it.

```solidity
uint defaultValue;
uint explicitValue = 0;

// (defaultValue == explicitValue) <-- true
```

Types can be cast from one type to another, but not as freely as you may expect. For example, to convert a `uint256` into a `int8`, you need to cast twice:

```solidity
uint256 first = 1;
int8 second = int8(int256(first));
```

:::danger

Overflow/underflow protection (described below), does not provide protection when casting.

```solidity
uint256 first = 256;
int8 second = int8(int256(first)); // <- The value stored in second is 0
```

:::

## Boolean

[Booleans] can have a value of `true` or `false`. Solidity does not have the concept of _truthy_ or _falsey_, and non-boolean values cannot be cast to bools by design. The short conversation in this [issue] explains why, and explains the philosophy why.

### Logical Operators

Standard logical operators (`!`, `&&`, `||`, `==`, `!=`) apply to booleans. Short-circuiting rules do apply, which can sometimes be used for gas savings since if the first operator in an `&&` is `false` or `||` is `true`, the second will not be evaluated. For example, the following code will execute without an error, despite the divide by zero in the second statement.

```solidity
// Bad code for example.  Do not use.
uint divisor = 0;
if(1 < 2 || 1 / divisor > 0) {
    // Do something...
}
```

You cannot use any variant of `>` or `<` with booleans, because they cannot be implicitly or explicitly cast to a type that uses those operators.

---

## Numbers

Solidity has a number of types for signed and unsigned [integers], which are not ignored as much as they are in other languages, due to potential gas-savings when storing smaller numbers. Support for [fixed point numbers] is under development, but is not fully implemented as of version `0.8.17`.

Floating point numbers are not supported and are not likely to be. Floating precision includes an inherent element of ambiguity that doesn't work for explicit environments like blockchains.

### Min, Max, and Overflow

Minimum and maximum values for each type can be accessed with `type(<type>).min` and `type(<type>).max`. For example, `type(uint).min` is **0**, and `type(uint).max` is equal to **2^256-1**.

An overflow or underflow will cause a transaction to _revert_, unless it occurs in a code block that is marked as [unchecked].

### `uint` vs. `int`

In Solidity, it is common practice to favor `uint` over `int` when it is known that a value will never (or should never) be below zero. This practice helps you write more secure code by requiring you to declare whether or not a given value should be allowed to be negative. Use `uint` for values that should not, such as array indexes, account balances, etc. and `int` for a value that does **need** to be negative.

### Integer Variants

Smaller and larger variants of integers exist in many languages but have fallen out of favor in many instances, in part because memory and storage are relatively cheap. Solidity supports sizes in steps of eight from `uint8` to `uint256`, and the same for `int`.

Smaller sized integers are used to optimize gas usage in storage operations, but there is a cost. The EVM operates with 256 bit words, so operations involving smaller data types must be cast first, which costs gas.

`uint` is an alias for `uint256` and can be considered the default.

### Operators

Comparisons (`<=`, `<`, `==`, `!=`, `>=`, `>`) and arithmetic (`+`, `-`, `*`, `/`, `%`, `**`) operators are present and work as expected. You can also use bit and shift operators.

`uint` and `int` variants can be compared directly, such as `uint8` and `uint256`, but you must cast one value to compare a `uint` to an `int`.

```solidity
uint first = 1;
int8 second = 1;

if(first == uint8(second)) {
    // Do something...
}
```

---

## Addresses

The [address] type is a relatively unique type representing a wallet or contract address. It holds a 20-byte value, similar to the one we explored when you deployed your _Hello World_ contract in _Remix_. `address payable` is a variant of `address` that allows you to use the `transfer` and `send` methods. This distinction helps prevent sending Ether, or other tokens, to a contract that is not designed to receive it. If that were to happen, the Ether would be lost.

Addresses are **not** strings and do not need quotes when represented literally, but conversions from `bytes20` and `uint160` are allowed.

```solidity
address existingWallet = 0xd9145CCE52D386f254917e481eB44e9943F39138;
```

### Members of Addresses

Addresses contain a number of functions. `balance` returns the balance of an address, and `transfer`, mentioned above, can be used to send `ether`.

```solidity
function getBalance(address _address) public view returns(uint) {
    return _address.balance;
}
```

Later on, you'll learn about `call`, `delegatecall`, and `staticcall`, which can be used to call functions deployed in other contracts.

---

## Contracts

When you declare a [contract], you are defining a type. This type can be used to instantiate one contract as a local variable inside a second contract, allowing the second to interact with the first.

---

## Byte Arrays and Strings

[Byte arrays] come as both fixed-size and dynamically-sized. They hold a sequence of bytes. Arrays are a little more complicated than in other languages and will be covered in-depth later.

### Strings

Strings are arrays in Solidity, not a type. You cannot concat them with `+`, but as of _0.8.12_, you can use `string.concat(first, second)`. They are limited to printable characters and escaped characters. Casting other data types to `string` is at best tricky, and sometimes impossible.

Generally speaking, you should be deliberate when working with strings inside of a smart contract. Don't be afraid to use them when appropriate, but if possible, craft and display messages on the front end rather than spending gas to assemble them on the back end.

---

## Enums

[Enums] allow you to apply human-readable labels to a list of unsigned integers.

```solidity
enum Flavors { Vanilla, Chocolate, Strawberry, Coffee }

Flavors chosenFlavor = Flavors.Coffee;
```

Enums can be explicitly cast to and from `uint`, but not implicitly. They are limited to 256 members.

---

## Constant and Immutable

The [constant and immutable] keywords allow you to declare variables that cannot be changed. Both result in gas savings because the compiler does not need to reserve a storage slot for these values.

As of _0.8.17_, `constant` and `immutable` are not fully implemented. Both are supported on [value types], and `constant` can also be used with strings.

### Constant

Constants can be declared at the file level, or at the contract level. In Solidity, modifiers come after the type declaration. You must initialize a value when declaring a constant. Convention is to use SCREAMING_SNAKE_CASE for constants.

```solidity
uint constant NUMBER_OF_TEAMS = 10;

contract Cars {
    uint constant NUMBER_OF_CARS = 20;
}
```

At compilation, the compiler replaces every instance of the constant variable with its literal value.

### Immutable

The immutable keyword is used to declare variables that are set once within the constructor, which are then never changed:

```solidity
contract Season {
    immutable numberOfRaces;

    constructor(uint _numberOfRaces) {
        numberOfRaces = _numberOfRaces;
    }
}
```

---

## Conclusion

You've learned the usage and some of the unique quirks of common variable types in Solidity. You've seen how overflow and underflow are handled and how that behavior can be overridden. You've learned why unsigned integers are used more commonly than in other languages, why floats are not present, and have been introduced to some of the quirks of working with strings. Finally, you've been introduced to the address and contract data types.

---

[types]: https://docs.soliditylang.org/en/v0.8.17/types.html
[Booleans]: https://docs.soliditylang.org/en/v0.8.17/types.html#booleans
[issue]: https://github.com/ethereum/solidity/issues/1200
[integers]: https://docs.soliditylang.org/en/v0.8.17/types.html#integers
[fixed point numbers]: https://docs.soliditylang.org/en/v0.8.17/types.html#fixed-point-numbers
[unchecked]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html#unchecked
[address]: https://docs.soliditylang.org/en/v0.8.17/types.html#address
[contract]: https://docs.soliditylang.org/en/v0.8.17/types.html#contract-types
[Byte arrays]: https://docs.soliditylang.org/en/v0.8.17/types.html#fixed-size-byte-arrays
[Enums]: https://docs.soliditylang.org/en/v0.8.17/types.html#enums
[constant and immutable]: https://docs.soliditylang.org/en/v0.8.17/contracts.html?constant-and-immutable-state-variables#constant-and-immutable-state-variables
[value types]: https://docs.soliditylang.org/en/v0.8.17/types.html#value-types



<!-- File: ../web/apps/base-docs/base-learn/docs/contracts-and-basic-functions/intro-to-contracts-vid.md -->

---
title: Introduction to Contracts
description: Learn about the core structure of EVM programs.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035762' title='Introduction to Contracts' />



<!-- File: ../web/apps/base-docs/base-learn/docs/contracts-and-basic-functions/hello-world-step-by-step.md -->

---
title: Hello World
description: Write your first contract with Solidity.
hide_table_of_contents: false
---

As is tradition, we'll begin coding with a variant of "Hello World" written as a smart contract. There isn't really a console to write to\*, so instead, we'll write a contract that says hello to the sender, using the name they provide.

\*You will be able to use `console.log` with _Hardhat_, with some restrictions.

---

## Objectives

By the end of this lesson you should be able to:

- Construct a simple "Hello World" contract
- List the major differences between data types in Solidity as compared to other languages
- Select the appropriate visibility for a function

---

## Hello World

Writing "Hello World" in a smart contract requires a little more consideration than in other languages. Your code is deployed remotely, but it isn't running on a server where you can access logs, or on your local machine where you have access to a console. One way to do it is to write a function that returns "Hello World".

### Creating the Contract

To create a contract:

1. Create a new workspace in Remix.
2. Name it `Hello World` and delete the `.deps` folder.
3. Leave `.prettierrc.json` and click the settings gear in the bottom left.
4. Uncheck the top option to _Generate contract metadata..._
5. Open the _Solidity Compiler_ plugin and enable _Auto compile_.
6. Create a new folder called `contracts`, and within that folder, create a file called `hello-world.sol`.

Solidity files usually start with a comment containing an [_SPDX-License-Identifier_]. It's not a requirement, but there are a couple of advantages to doing this. First, everything you deploy on the blockchain is public. This doesn't mean you are giving away everything you deploy for free, nor does it mean you have the right to use the code from any deployed contract. The license determines allowed usage and is generally protected by international copyright laws, the same as any other code.

If you don't want to give a license, you can put `UNLICENSED`. Common open source licenses, such as `MIT` and `GPL-3.0` are popular as well. Add your license identifier:

```Solidity
// SPDX-License-Identifier: MIT
```

Below the license identifier, you need to specify which [version] of Solidity the compiler should use to compile your code. If by the time you read this, the version has advanced, you should try to use the most current version. Doing so may cause you to run into unexpected errors, but it's great practice for working in real-world conditions!

```Solidity
pragma solidity 0.8.17;
```

Finally, add a `contract` called `HelloWorld`. You should end up with:

```Solidity
// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

contract HelloWorld {

}
```

### SayHello Function

Add a function to your contract called `SayHello`:

```Solidity
function SayHello() {

}
```

You'll get a compiler syntax error for _No visibility specified. Did you intend to add "public"?_.

Is `public` the most appropriate [visibility specifier]?

It would work, but you won't be calling this function from within the contract, so `external` is more appropriate.

You also need to specify a return type, and we've decided this function should return a string. You'll learn more about this later, but in Solidity, many of the more complex types require you to specify if they are `storage` or `memory`. You can then have your function return a string of `"Hello World!"`.

Don't forget your semicolon. They're mandatory in Solidity!

You should have:

```Solidity
function SayHello() external returns (string memory) {
    return "Hello World!";
}
```

Before you deploy, check the `Compiler` plugin. You've got one last warning:

> Warning: Function state mutability can be restricted to pure

[Modifiers] are used to modify the behavior of a function. The `pure` modifier prevents the function from modifying, or even accessing state. While not mandatory, using these modifiers can help you and other programmers know the intention and impact of the functions you write. Your final function should be similar to:

```Solidity
function SayHello() external pure returns (string memory) {
    return "Hello World!";
}
```

### Deployment and Testing

Confirm that there is a green checkmark on the icon for the compiler plugin, and then switch to the _Deploy & Run Transactions_ plugin.

Click the _Deploy_ button and your contract should appear in _Deployed Contracts_. Open it up and then click the _SayHello_ button. Did it work?

You should see your message below the button. Another option to see the return for your `HelloWorld` function is to expand the entry in the console. You should see a _decoded output_ of:

```text
{
	"0": "string: Hello World!"
}
```

---

## Greeter

Now, let's modify your say hello function to greet a user by name, instead of just saying "Hello World!"

### First Pass Attempt

You'd probably expect this to be pretty easy. Start by changing the name of the function (or adding a new one) to `Greeter` and giving it a parameter for a `string memory _name`. The underscore is a common convention to mark functions and variables as internal to their scope. Doing so helps you tell the difference between a storage variable, and a memory variable that only exists within the call.

Finally, try creating a return string similar to how you might in another language with `"Hello " + _name`. You should have:

```Solidity
// Bad code example: Does not work
function Greeter(string memory _name) external pure returns (string memory) {
    return "Hello " + _name + "!";
}
```

Unfortunately, this does not work in Solidity. The error message you receive is a little confusing:

> TypeError: Operator + not compatible with types literal_string "Hello" and string memory.

You might think that there is some sort of type casting or conversion error that could be solved by explicitly casting the string literal to string memory, or vice versa. This is a great instinct. Solidity is a very explicit language.

However, you receive a similar error with `"Hello " + "world"`.

String concatenation is possible in Solidity, but it's a bit more complicated than most languages, for good reason. Working with string costs a large amount of gas, so it's usually better to handle this sort of processing on the front end.

### Plan B

We still want to return something with the name provided by the user, so let's try something a little different. Solidity is a _variadic_ language, which means it allows functions to return more than one value.

Modify your return declaration: `returns (string memory, string memory)`

Now, your function can return a [tuple] containing two strings!

`return ("Hello", _name)`;

Deploy and test your contract. You should get a _decoded output_ with:

```text
{
	"string _name": "Your Name"
}
```

### Full Example Code

```solidity
// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

contract HelloWorld {

    function SayHello() external pure returns (string memory) {
        return "Hello World!";
    }

    // Bad code example: Does not work
    // function Greeter(string memory _name) external pure returns (string memory) {
    //     return "Hello " + _name;
    // }

    function Greeter(string memory _name) external pure returns (string memory, string memory) {
        return ("Hello", _name);
    }
}
```

---

## Conclusion

Congratulations! You've written and tested your first smart contract! You selected a license and a version of Solidity. You declared a contract and added a function that returns a value.

You also learned more about some of the ways in which Solidity is more challenging to work with than other languages, and the additional elements you sometimes need to declare functions and types.

---

<!-- Add reference style links here.  These do not render on the page. -->

[_SPDX-License-Identifier_]: https://spdx.org/licenses/
[version]: https://docs.soliditylang.org/en/v0.8.17/layout-of-source-files.html?#version-pragma
[visibility specifier]: https://docs.soliditylang.org/en/v0.8.17/cheatsheet.html?#function-visibility-specifiers
[modifiers]: https://docs.soliditylang.org/en/v0.8.17/cheatsheet.html?#modifiers
[tuple]: https://en.wikipedia.org/wiki/Tuple



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/erc-20-testing-vid.md -->

---
title: ERC-20 Testing
description: Test the OpenZeppelin ERC-20 implementation.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035929' title='ERC-20 Testing' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/erc-20-token-sbs.md -->

---
title: ERC-20 Implementation
description: Implement your own ERC-20 token.
hide_table_of_contents: false
---

The ERC-20 is a standard that allows for the development of fungible tokens and helps sites and apps, such as exchanges, know how to find and display information about these tokens. You can leverage existing implementations, such as the one by [OpenZeppelin] to develop your own tokens.

---

## Objectives

By the end of this lesson you should be able to:

- Describe OpenZeppelin
- Import the OpenZeppelin ERC-20 implementation
- Describe the difference between the ERC-20 standard and OpenZeppelin's ERC20.sol
- Build and deploy an ERC-20 compliant token

---

## Setting Up the Contract

Create a new Solidity file, add the license and pragma, and import the ERC-20 implementation linked above.

Add a contract called `MyERC20Token` that inherits from `ERC20`.

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";

contract MyERC20Token is ERC20 {

}
```

### Adding a Constructor

Review the constructor on line 53 of the [OpenZeppelin] implementation. It requires strings for the name and symbol you wish to use for your token. They're using a slightly different naming convention by putting the `_` after the name of the parameters. Like any other function, you can pass variables of **any** name as long as they're the right type, so feel free to continue adding the `_` in front in your contract's constructor:

```solidity
constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {

}
```

:::caution

There is neither a governing body nor built-in programmatic rules preventing you, or anyone else, from using the same name and symbol as an already in-use token. Scammers often take advantage of this fact, and even well-meaning developers can cause confusion by not being careful here.

:::

That's it. You're done! Deploy and test, and you should see all of the functionality called for by the standard and provided by the OpenZeppelin implementation.

![Deployed](../../assets/images/erc-20/deployed-token.png)

Do some testing. You'll see that the `totalSupply` and all balances are zero.

By default, the decimal for the token will be 18, which is the most common choice. Remember, there aren't decimal types yet, so 1.0 ETH is really a `uint` holding 1 \* 10\*\*18, or 1000000000000000000.

---

## ERC-20 Further Testing

Line 251 of the [OpenZeppelin] implementation contains a `_mint` function, but it's internal. As a result, you'll need to figure out a minting mechanism and add it via your own contract.

### Minting in the Constructor

One method of using the `_mint` function is to create an initial supply of tokens in the constructor. Add a call to `_mint` that awards 1 full token to the contract creator. Remember, the decimal is 18. Minting literally `1` is creating a tiny speck of dust.

```solidity
constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
    _mint(msg.sender, 1 * 10**18);
}
```

Redeploy. Without you needing to do anything, you should find that the `totalSupply` is now 1000000000000000000, as is the `balanceOf` the deploying address.

You can also use this to mint to other users. Go ahead and add the second and third accounts:

<details>

<summary>Reveal code</summary>

```solidity
constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
    _mint(msg.sender, 1 * 10**18);
    _mint(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2, 1 * 10**18);
    _mint(0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db, 1 * 10**18);
}
```

</details>

<br/>


**Switch back** to the first account and redeploy. Test to confirm that each account has the appropriate amount of tokens.

### Testing the Transfer Function

Try using the `transfer` function to move tokens around.

What happens if you try to burn a token by sending it to the zero address? Give it a try!

You'll get an error, because protecting from burning is built into the `_transfer` function.

```text
transact to MyERC20Token.transfer pending ...
transact to MyERC20Token.transfer errored: VM error: revert.

revert
	The transaction has been reverted to the initial state.
Reason provided by the contract: "ERC20: transfer to the zero address".
Debug the transaction to get more information.
```

### Testing the Transfer From Function

You might have noticed that there's another function called `transferFrom`. What's that for? Check the documentation in the contract to find out!

This function works with the `allowance` function to give the owner of one wallet permission to spend up to a specified amount of tokens owned by another. Exchanges can make use of this to allow a user to post tokens for sale at a given price without needing to take possession of them.

---

## ERC-20 Final Thoughts

The world is still figuring out how to handle all of the new possibilities tokens provide. Old laws are being applied in new ways, and new laws are being written. Different jurisdictions are doing this in unique and sometimes conflicting ways.

You should consult with a lawyer in your jurisdiction before releasing your own tokens.

---

## Conclusion

In this lesson, you've learned how easy it is to create an ERC-20 compliant token by using the OpenZeppelin implementation. You've reviewed at least one method to mint an initial supply of tokens, and that it's up to you to figure out the best way to create your tokens and follow all relevant laws and regulations.

---

[OpenZeppelin]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/erc-20-standard.md -->

---
title: The ERC-20 Token Standard
description: An overview of the ERC-20 token standard
hide_table_of_contents: false
---

In this article, we'll delve into the structure and specifications of ERC-20 tokens, uncovering the key elements that contribute to their widespread adoption and diverse use cases.

---

## Objectives:

By the end of this lesson you should be able to:

- Analyze the anatomy of an ERC-20 token
- Review the formal specification for ERC-20

---

## Introduction

The emergence of the ERC-20 token standard marked a significant milestone in the evolution of the Ethereum ecosystem, providing a unified and adaptable framework for creating and managing fungible tokens. As the backbone for a vast array of applications in decentralized finance and beyond, ERC-20 tokens facilitate seamless collaboration and interoperability within the Ethereum ecosystem. Their adaptable nature and standardized structure have made them the go-to choice for developers and users alike, laying the groundwork for continued innovation and growth in the Ethereum space.

The ERC-20 token standard has not only streamlined the creation of new tokens but also bolstered the overall user experience by establishing a consistent set of rules and functions. As a result, it has garnered widespread adoption and solidified its position as the de facto standard for fungible tokens on Ethereum, driving the expansion of the decentralized economy and fostering the development of novel applications and services.

![The Evolution of the Ethereum Ecosystem](../../assets/images/erc-20/evolution-eth-erc20.png)

---

## ERC-20 Specification

EIP-20 (Ethereum Improvement Proposal 20) is the formal specification for ERC-20, defining the requirements to create compliant tokens on the Ethereum blockchain. EIP-20 prescribes the mandatory functions, optional functions, and events a token must implement to achieve ERC-20 compliance. Adherence to EIP-20 allows developers to create tokens compatible with existing Ethereum applications and services, streamlining integration.

---

## Anatomy of an ERC-20 Token

An ERC-20 token consists of a smart contract that implements the standardized interface, which comprises a set of six mandatory functions:

- **totalSupply():** Returns the total supply of the token.
- **balanceOf(address):** Provides the balance of tokens held by a specific address.
- **transfer(address, uint256):** Transfers a specified amount of tokens from the sender's address to the specified recipient's address.
- **transferFrom(address, address, uint256):** Enables a third party to transfer tokens on behalf of the token owner, given that the owner has approved the transaction.
- **approve(address, uint256):** Allows the token owner to grant permission to a third party to spend a specified amount of tokens on their behalf.
- **allowance(address, address):** Returns the amount of tokens the token owner has allowed a third party to spend on their behalf.

Additionally, ERC-20 tokens can include optional functions that provide descriptive information about the token:

- **name():** Returns the name of the token, for example, "Uniswap."
- **symbol():** Provides the token's symbol, like "UNI."
- **decimals():** Indicates the number of decimal places the token can be divided into, typically 18 for most tokens.

---

## Benefits of ERC-20 Standardization

The standardization of ERC-20 tokens provides several benefits for both developers and users. For developers, it simplifies the process of creating new tokens by providing a consistent set of functions and conventions. This reduces the likelihood of errors and ensures a smooth integration with existing applications and services in the Ethereum ecosystem.

![ERC-20 Standardization Developer's Perspective](../../assets/images/erc-20/erc20-dev-perspective.png)

For users, the standardized interface makes it easier to interact with a wide variety of tokens, regardless of their specific purpose or implementation. This means that users can effortlessly check their token balance, transfer tokens, or approve transactions using the same set of functions, whether they are interacting with a governance token like UNI or a stablecoin like USDC.

![ERC-20 Standardization User's Perspective](../../assets/images/erc-20/erc20-user-perspective.png)

---

## Applications

ERC-20 tokens find wide-ranging applications in various categories, each with its unique purpose and functionality:

- **Utility tokens:** These tokens can be used to access specific services or features within a platform. Examples include Filecoin (FIL) for decentralized storage, Basic Attention Token (BAT) for digital advertising, and Decentraland's MANA for purchasing virtual land and assets.

- **Governance tokens:** These tokens grant voting rights and influence over the development of a project, allowing holders to participate in decision-making processes. Examples include Uniswap (UNI), Aave (AAVE), and Compound (COMP).

- **Stablecoins:** These tokens maintain a relatively stable value pegged to a reserve of assets or fiat currency, providing a less volatile option for transactions and trading. Examples include USD Coin (USDC), Tether (USDT), and MakerDAO's DAI.

- **Liquidity tokens:** Liquidity providers on DeFi platforms often receive ERC-20 tokens as a representation of their share in a liquidity pool. These tokens can be staked or traded, and they enable users to earn rewards for providing liquidity. Examples include Uniswap LP tokens and Curve LP tokens.

- **Rewards tokens:** Some platforms issue ERC-20 tokens as incentives for users to participate in their ecosystem, such as staking, lending, or providing liquidity. These tokens can be earned as passive income or used to access additional platform features. Examples include Synthetix (SNX) and SushiSwap (SUSHI).

Each of these use cases demonstrates the adaptability of ERC-20 tokens to serve different needs within the blockchain ecosystem.

---

## Conclusion

By providing a consistent framework for fungible tokens and adhering to the formal EIP-20 specification, ERC-20 has enabled the development of countless projects and applications that have revolutionized how value is exchanged and managed on Ethereum. Analyzing the anatomy of an ERC-20 token and reviewing its formal specification reveal the versatility and importance of this token standard.

---

## See Also

- [Introduction to Ethereum Improvement Proposals (EIPs)](https://ethereum.org/en/eips/)
- [EIP-20: ERC-20 Token Standard](https://eips.ethereum.org/EIPS/eip-20)
- [ERC-20 Token Standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/erc-20-exercise.md -->

---
title: ERC-20 Tokens Exercise
description: Exercise - Create your own ERC-20 token!
hide_table_of_contents: false
---

Create a contract that adheres to the following specifications.

---

## Contract

Create a contract called `WeightedVoting`. Add the following:

- A `maxSupply` of 1,000,000
- Errors for:
  - `TokensClaimed`
  - `AllTokensClaimed`
  - `NoTokensHeld`
  - `QuorumTooHigh`, returning the quorum amount proposed
  - `AlreadyVoted`
  - `VotingClosed`
- A struct called `Issue` containing:
  - An OpenZeppelin Enumerable Set storing addresses called `voters`
  - A string `issueDesc`
  - Storage for the number of `votesFor`, `votesAgainst`, `votesAbstain`, `totalVotes`, and `quorum`
  - Bools storing if the issue is `passed` and `closed`

:::caution

The unit tests require this `struct` to be constructed with the variables in the order above.

:::

- An array of `Issue`s called `issues`
- An `enum` for `Vote` containing:
  - `AGAINST`
  - `FOR`
  - `ABSTAIN`
- Anything else needed to complete the tasks

Add the following functions.

### Constructor

Initialize the ERC-20 token and burn the zeroeth element of `issues`.

### Claim

Add a `public` function called `claim`. When called, so long as a number of tokens equalling the `maximumSupply` have not yet been distributed, any wallet _that has not made a claim previously_ should be able to claim 100 tokens. If a wallet tries to claim a second time, it should revert with `TokensClaimed`.

Once all tokens have been claimed, this function should revert with an error `AllTokensClaimed`.

:::caution

In our simple token, we used `totalSupply` to mint our tokens up front. The ERC20 implementation we're using also tracks `totalSupply`, but does it differently.

Review the docs and code comments to learn how.

:::

### Create Issue

Implement an `external` function called `createIssue`. It should add a new `Issue` to `issues`, allowing the user to set the description of the issue, and `quorum` - which is how many votes are needed to close the issue.

Only token holders are allowed to create issues, and issues cannot be created that require a `quorum` greater than the current total number of tokens.

This function must return the index of the newly-created issue.

:::caution

One of the unit tests will break if you place your check for `quorum` before the check that the user holds a token. The test compares encoded error names, which are **not** human-readable. If you are getting `-> AssertionError: �s is not equal to �9�` or similar, this is likely the issue.

:::

### Get Issue

Add an `external` function called `getIssue` that can return all of the data for the issue of the provided `_id`.

`EnumerableSet` has a `mapping` underneath, so it can't be returned outside of the contract. You'll have to figure something else out.

:::info Hint

The return type for this function should be a `struct` very similar to the one that stores the issues.

:::

### Vote

Add a `public` function called `vote` that accepts an `_issueId` and the token holder's vote. The function should revert if the issue is closed, or the wallet has already voted on this issue.

Holders must vote all of their tokens for, against, or abstaining from the issue. This amount should be added to the appropriate member of the issue and the total number of votes collected.

If this vote takes the total number of votes to or above the `quorum` for that vote, then:

- The issue should be set so that `closed` is true
- If there are **more** votes for than against, set `passed` to `true`

---

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

:::caution

The contract specification contains actions that can only be performed once by a given address. As a result, the unit tests for a passing contract will only be successful the **first** time you test.

**You may need to submit a fresh deployment to pass**

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={14}/>



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/analyzing-erc-20-vid.md -->

---
title: Analyzing the ERC-20 Standard
description: Explore the ERC-20 standard.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035875' title='Analyzing the ERC-20 Token' />



<!-- File: ../web/apps/base-docs/base-learn/docs/erc-20-token/openzeppelin-erc-20-vid.md -->

---
title: OpenZeppelin ERC-20 Implementation
description: Review a popular implementation of the ERC-20 standard.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='805035901' title='OpenZeppelin ERC-20' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-testing/contract-abi-and-testing-vid.md -->

---
title: Contract ABIs and Testing
description: Learn how the contract ABI is related to writing tests.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='840621876' title='Contract ABIs and Testing' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-testing/hardhat-testing-sbs.md -->

---
title: Testing with Hardhat and Typechain
description: Testing smart contracts with Hardhat and Typechain.
hide_table_of_contents: false
---

In this article, you'll learn how to test smart contracts with Hardhat and Typechain.

---

## Objectives

By the end of this lesson, you should be able to:

- Set up TypeChain to enable testing
- Write unit tests for smart contracts using Mocha, Chai, and the Hardhat Toolkit
- Set up multiple signers and call smart contract functions with different signers

---

## Overview

Testing is an important aspect of software development and developing smart contracts is no different. In fact, you need to be more careful because
smart contracts usually manage money and live in an adversarial environment, where anyone can see the code and interact with your smart contract. This means you can expect bad actors to try to exploit your smart contracts.

## Setup Typechain

In the previous guide, you created a new project using the `init` command that by default installs `@nomicfoundation/hardhat-toolbox`. This package already contains Typechain, which is a plugin that generates static types for your smart contracts. This means you can interact with your contracts and get immediate feedback about the parameters received by a particular function and the functions of a smart contract.

The best way to see its true potential is to start writing tests.

After compiling the hardhat project in the previous lesson, a new folder called `typechain-types` was created, which Typechain is already installed and running.

### Writing your first unit test with Typechain

Hardhat includes a sample smart contract named `Lock.sol` and a sample test inside the test folder named `Lock.ts`.

In the following, you reuse this smart contract but rewrite the test using Typechain.

To remove the body of the `Lock.ts` file:

```tsx
import { expect } from 'chai';
import { ethers } from 'hardhat';

describe('Lock', function () {});
```

Then, import two files from `typechain-types`, `Lock`, and `Lock__Factory`.

Typechain always creates two files per contract. The first one `Lock` refers to the type and functions of a particular contract. `Lock__Factory` is used to deploy the Lock contract or to create instances of a particular contract.

The `Lock.sol` contract allows the creator to lock Ether until an unlock time has passed.

Notice the constructor has a payable keyword:

```tsx
constructor(uint _unlockTime) payable {
        require(
            block.timestamp < _unlockTime,
            "Unlock time should be in the future"
        );

        unlockTime = _unlockTime;
        owner = payable(msg.sender);
    }
```

This means the contract is expecting to receive an amount of ether.

Next, test the following:

- The unlock time value
- The value locked during creation
- The owner address
- The withdraw function

<details>

<summary>Reveal code</summary>

Start with the value locked, however you must set up a `before` function, which will run before each test case.

Then, include some new imports and variables:

```tsx
import { expect } from 'chai';
import { ethers } from 'hardhat';

// A helper utility to get the timestamp.
import { time } from '@nomicfoundation/hardhat-network-helpers';

// We import this type to have our signers typed.
import { SignerWithAddress } from '@nomicfoundation/hardhat-ethers/signers';

// Types from typechain
import { Lock__factory, Lock } from '../typechain-types';

describe('Lock', function () {
  // This represents the time in the future we expect to release the funds locked.
  const UNLOCK_TIME = 10000;

  // The amount of ether we plan to lock.
  const VALUE_LOCKED = ethers.parseEther('0.01');

  // This variable will store the last block timestamp.
  let lastBlockTimeStamp: number;

  // Typechain allow us to type an instance of the Lock contract.
  let lockInstance: Lock;

  // This is the Signer of the owner.
  let ownerSigner: SignerWithAddress;

  // A non owner signed is useful to test non owner transactions.
  let otherUserSigner: SignerWithAddress;

  before(async () => {
    // We get the latest block.timestamp using the latest function of time.
    lastBlockTimeStamp = await time.latest();

    // Hardhat provide us with some sample signers that simulate Ethereum accounts.
    const signers = await ethers.getSigners();

    // We simply assign the first signer to ownerSigner
    ownerSigner = signers[0];

    // We assign the second signer to otherUserSigner
    otherUserSigner = signers[1];

    // We estimate unlockTime to be the last time stamp plus UNLOCK_TIME
    const unlockTime = lastBlockTimeStamp + UNLOCK_TIME;

    // Notice how we use the Lock__factory and pass a signer. Then we deploy by passing the unlockTime and the amount of ether we will lock.
    lockInstance = await new Lock__factory(ownerSigner).deploy(unlockTime, {
      value: VALUE_LOCKED,
    });
  });
});
```

</details>

### Testing `unlockTime`

Next, you include test cases after the `before` function.

The first test case should verify that the `unlockTime` variable is correct.

<details>

<summary>Reveal code</summary>

```tsx
it('should get the unlockTime value', async () => {
  // we get the value from the contract
  const unlockTime = await lockInstance.unlockTime();

  // We assert against the
  expect(unlockTime).to.equal(lastBlockTimeStamp + UNLOCK_TIME);
});
```

Notice how autocomplete appears after entering `lockInstance`:

![Auto complete](../../assets/images/hardhat-testing/autocomplete-unlockTime.png)

You can simply run `npx hardhat test` and then get:

```
  Lock
    ✔ should get the unlockTime value

  1 passing (1s)
```

</details>

### Testing Ether balance

In order to get the balance of your `Lock` contract, you simply call `ethers.provider.getBalance`.

Create a new test case:

<details>

<summary>Reveal code</summary>

```tsx
it('should have the right ether balance', async () => {
  // Get the Lock contract address
  const lockInstanceAddress = await lockInstance.getAddress();

  // Get the balance using ethers.provider.getBalance
  const contractBalance = await ethers.provider.getBalance(lockInstanceAddress);

  // We assert the balance against the VALUE_LOCKED we initially sent
  expect(contractBalance).to.equal(VALUE_LOCKED);
});
```

</details>
<br/>

Then, run `npx hardhat test` and you should get:

```
  Lock
    ✔ should get the unlockTime value
    ✔ should have the right ether balance

  2 passing (1s)
```

### Testing `owner`

Similar to the previous test cases, you can verify that the owner is correct.

<details>

<summary>Reveal code</summary>

```tsx
it('should have the right owner', async () => {
  // Notice ownerSigned has an address property
  expect(await lockInstance.owner()).to.equal(ownerSigner.address);
});
```

</details>
<br/>

Then, run `npx hardhat test` and you should get:

```
  Lock
    ✔ should get the unlockTime value
    ✔ should have the right ether balance
    ✔ should have the right owner

  3 passing (1s)
```

### Testing withdraw

Testing withdrawal is more complex because you need to assert certain conditions, such as:

- The owner cannot withdraw before the unlock time.
- Only the owner can withdraw.
- The withdraw function works as expected.

Hardhat allow you to test reverts with a set of custom matchers.

For example, the following code checks that an attempt to call the function `withdraw` reverts with a particular message:

```tsx
it('shouldn"t allow to withdraw before unlock time', async () => {
  await expect(lockInstance.withdraw()).to.be.revertedWith("You can't withdraw yet");
});
```

In addition, Hardhat also allows you to manipulate the time of the environment where the tests are executed. You can think of it as a Blockchain that is running before the tests and then the tests are executed against it.

You can modify `the block.timestamp` by using the time helper:

```tsx
it('shouldn"t allow to withdraw a non owner', async () => {
  const newLastBlockTimeStamp = await time.latest();

  // We set the next block time stamp using this helper.
  // We assign a value further in the future.
  await time.setNextBlockTimestamp(newLastBlockTimeStamp + UNLOCK_TIME);

  // Then we try to withdraw using other user signer. Notice the .connect function that is useful
  //  to create and instance but have the msg.sender as the new signer.
  const newInstanceUsingAnotherSigner = lockInstance.connect(otherUserSigner);

  // We attempt to withdraw, but since the sender is not the owner, it will revert.
  await expect(newInstanceUsingAnotherSigner.withdraw()).to.be.revertedWith("You aren't the owner");
});
```

Finally, test that the owner can withdraw. You can manipulate the time similarly to the previous test case but you won't change the signer and will assert the new balances.

<details>

<summary>Reveal code</summary>

```tsx
it('should allow to withdraw an owner', async () => {
  const balanceBefore = await ethers.provider.getBalance(await lockInstance.getAddress());

  // Its value will be the one we lock at deployment time.
  expect(balanceBefore).to.equal(VALUE_LOCKED);

  const newLastBlockTimeStamp = await time.latest();

  // We increase time
  await time.setNextBlockTimestamp(newLastBlockTimeStamp + UNLOCK_TIME);

  // Attempt to withdraw
  await lockInstance.withdraw();

  // Get new balance and assert that is 0
  const balanceAfter = await ethers.provider.getBalance(await lockInstance.getAddress());
  expect(balanceAfter).to.equal(0);
});
```

</details>

<br/>

You can then run `npx hardhat test` and you should get:

```
  Lock
    ✔ should get the unlockTime value
    ✔ should have the right ether balance
    ✔ should have the right owner
    ✔ shouldn"t allow to withdraw before unlock time (51ms)
    ✔ shouldn"t allow to withdraw a non owner
    ✔ should allow to withdraw an owner

  6 passing (2s)
```

## Conclusion

In this lesson, you've learned how to test smart contracts using Hardhat and Typechain.

---

## See also

[Solidity Docs](https://docs.soliditylang.org/en/v0.8.17/)
[Remix Project]: https://remix-project.org/
[Hardhat]: https://hardhat.org/



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-testing/writing-tests-vid.md -->

---
title: Writing Tests
description: An introduction to writing tests.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='840620773' title='Testing Overview' />



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-testing/testing-overview-vid.md -->

---
title: Testing Overview
description: An overview of writing tests in Hardhat.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='840618938' title='Testing Overview' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/anatomy-of-a-smart-contract-vid.md -->

---
title: Anatomy of a Smart Contract
description: Review how smart contracts are organized.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='816714891' title='Anatomy of a Smart Contract' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/introduction-to-remix-vid.md -->

---
title: Introduction to Remix
description: Learn about the Remix online IDE.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804478378' title='Introduction to Remix' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/deployment-in-remix-vid.md -->

---
title: Deployment in Remix
description: Learn to deploy your contracts to the Remix VM.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='804476884' title='Deployment in Remix' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/solidity-overview.md -->

---
title: 'Solidity Overview'
description: An overview of the Solidity programming language.
hide_table_of_contents: false
---

In this article, you'll learn about the origins and history of Solidity, where to find the docs, and review some of the considerations that make programming in Solidity relatively unique. You'll also learn about how to get started with development!

---

## Objectives

By the end of this lesson you should be able to:

- Describe why languages like Solidity are used to write smart contracts
- Relate an overview of the history (and pace of change) of Solidity and its strengths and weaknesses

---

## Introduction to Solidity

Solidity is a high-level language used to develop smart contracts compatible with the Ethereum Virtual Machine. It is object-oriented, strongly typed, and allows variadic (more than one argument) returns. Solidity was [inspired] by a number of languages, particularly C++. Compared to other languages, Solidity changes very rapidly. Review the [releases] to see just how rapid!

### The Docs

The [Solidity Docs] are thorough and helpful. This guide will regularly reference them and they should be your first source for specific information related to any of the components in the language. As with any versioned doc source, always double-check that the version you're referencing matches the version you are developing with.

### Origins TL;DR

Solidity was developed by the Ethereum Project's Solidity team and was first previewed in 2014 at DevCon0. The original goal was to create an easy-to-use language for smart contract development. A great [history overview] can be found in the team's blog.

### What it Actually Does

Solidity is very similar to the programming languages you are familiar with in that it's a high-level language that is relatively human-readable, which is then compiled into byte-code that can be read by the EVM. For example, this:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract Hello {
    function HelloWorld() public pure returns (string memory) {
        return "Hello World!";
    }
}
```

compiles into this:

```text
0x608060405234801561001057600080fd5b50610173806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c80637fffb7bd14610030575b600080fd5b61003861004e565b604051610045919061011b565b60405180910390f35b60606040518060400160405280600c81526020017f48656c6c6f20576f726c64210000000000000000000000000000000000000000815250905090565b600081519050919050565b600082825260208201905092915050565b60005b838110156100c55780820151818401526020810190506100aa565b60008484015250505050565b6000601f19601f8301169050919050565b60006100ed8261008b565b6100f78185610096565b93506101078185602086016100a7565b610110816100d1565b840191505092915050565b6000602082019050818103600083015261013581846100e2565b90509291505056fea2646970667358221220575a1ec2ade1712a7a3a4e91cc5d83212207e4a5c70f5b2bc50079ee65ad29b364736f6c63430008110033
```

As you can see, the first example is a little easier to read!

---

## Programming for Ethereum with Solidity

On the surface, writing code for the EVM using Solidity isn't particularly different from other programming languages. You write code organized into functions, and those functions get executed when called, often accepting arguments and returning values. However, there are a number of unusual traits that will require you to think a little differently. Additionally, the EVM is a much smaller, slower, and less-powerful computer than a desktop, or even a mobile device.

### Gas Fees

Every single [operation] your code performs costs gas, which your users pay for. You're probably already well-versed in _[time complexity]_ and know how to get an operation down to _O(log(n))_, when you have no choice but to run something that is _O(2^n)_, and that sometimes, nested for-loops go brrrrr. These constraints and practices still apply, but in Solidity, every inefficiency directly costs your users money, which can make your app more expensive, and less appealing, than needed.

When you were learning about _time complexity_, you probably heard the term _space complexity_ once, and then it was never mentioned again. This is because normally, computation is expensive, and storage is practically free. The opposite is true on the EVM. It costs a minimum of **20,000** gas to initialize a variable, and a minimum of **5,000** to change it. Meanwhile, the cost to add two numbers together is **3** gas. This means it is often much cheaper to repeatedly derive a value that is calculated from other values than it is to calculate it once and save it.

You also have to be careful to write code with predictable execution paths. Each transaction is sent with a gas limit and which various frameworks, such as _ethers.js_, in order to do their best to estimate. If this estimate is wrong, the transaction will fail, but **it will still cost the gas used up until the point it failed!**

### Contract Size Limit

[EIP-170] introduced a compiled byte-code size limit of **24 KiB** (24,576 B) to Ethereum Smart Contracts. Read that sentence again, as you're probably not used to thinking in this small of a number!

While there isn't an exact ratio of lines of code to compiled byte-code size, you're limited to deploying contracts that are approximately 300-500 lines of Solidity.

Luckily, there are a few ways around this limitation. Contracts can expose their functions to be called by other contracts, although there is an additional cost. Using this, you can write a suite of contracts designed to work together, or even make use of contracts already deployed by others. You can also use more advanced solutions, such as [EIP-2535].

### Stack Limit

Programs written for computers or mobile devices often work with hundreds of variables at the same time. The EVM operates with a stack that can hold 1,024 values, but it can only access the top 16.

There are many implications of this limit, but the one you'll run into most commonly is the "Stack too Deep" error because you're trying to work with too many variables at once.

In Solidity/EVM, your functions are limited to a total of 16 variables that are input, output, or initialized by the function.

### Permanence

Once deployed, smart contracts are permanent and cannot be changed by anyone, **even their creator(s)!** It is literally not possible to edit them. If the creators of a contract discover a vulnerability, they can't do anything about it except withdraw the funds - if the contract allows them to!

As a result, standard practice is to have a smart contract audited by an expert, before deployment.

### Pace of Change

Solidity files always start with a license and a version:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.17;
```

One of the reasons for this is that the pace of development for Solidity is **very** fast, and changes are not always backwards-compatible. As a result, the compiler needs to know which version to use when converting the Solidity code to byte-code.

Review the [changelog] to see some of the recent additions and fixes.

---

## Development Environments

We'll be covering two tools that can be used to develop in Solidity.

### Remix

We'll start with [Remix], an online IDE similar to Codepen, Replit, or CodeSandbox. Remix is a great place to get started because it works out of the box, has a number of demo contracts, and has great debugging tools. More information can be found at the [Remix Project] website.

![Remix Home](../../assets/images/introduction-to-solidity/remix-home.png)

:::danger

**BE VERY CAREFUL** while using Remix, as it can also be used by scammers. Remix itself will warn you about this, so take heed! One common scam is for the scammer to convince you to paste and deploy code that is allegedly some sort of automated moneymaker, such as a staking tool, or a bot.

If you paste and run code that you don't understand, you may lose all assets from your currently connected wallet. You should also be careful to always navigate directly to `remix.ethereum.org`. More experienced developers prefer to use static versions of Remix deployed to [IPFS], but be careful. There are also deployments that are compromised and used as a part of a scam!

:::

### Hardhat

[Hardhat] is a development environment that allows you to develop and test Solidity on your local machine. It includes debugging and unit testing tools, and has an ecosystem of third-party-developed plugins that ease development and deployment. Among other things, these plugins can help you deploy contracts, see the size of your compiled byte-code, and even see unit test coverage.

We'll introduce Hardhat and local development after the basics.

## Remix Setup

The next lesson will explore one of the demo contracts within [Remix]. Open it up and review the quickstart information if this is your first time on the site. Then, open or create a new workspace using the `Default` template.

**Delete** everything except the contracts folder and the `1_Storage.sol` contract within that folder. You can also leave `.prettierrc.json` if you'd like.

![Delete](../../assets/images/introduction-to-solidity/delete.png)

---

## Conclusion

On the surface, Solidity is very similar to other programming languages; most developers won't struggle to write familiar operations. However, there are some critically important properties to keep in mind. Operations are much more expensive than in other environments, particularly storage. You can use most of the practices you are accustomed to, but you are limited to very small contract sizes and by the size of the stack. Finally, remember that you should always use a separate wallet for development. If you make a mistake, you could lose anything in it!

---

## See also

[Solidity Docs](https://docs.soliditylang.org/en/v0.8.17/)

[inspired]: https://docs.soliditylang.org/en/v0.8.17/language-influences.html
[releases]: https://github.com/ethereum/solidity/releases
[Solidity Docs]: https://docs.soliditylang.org/en/v0.8.17/
[history overview]: https://blog.soliditylang.org/2020/07/08/solidity-turns-5/
[operation]: https://ethereum.org/en/developers/docs/evm/opcodes/
[time complexity]: https://en.wikipedia.org/wiki/Time_complexity
[EIP-170]: https://eips.ethereum.org/EIPS/eip-170
[EIP-2535]: https://eips.ethereum.org/EIPS/eip-2535
[changelog]: https://github.com/ethereum/solidity/blob/develop/Changelog.md
[Remix]: https://remix.ethereum.org/
[IPFS]: https://ipfs.tech/
[Remix Project]: https://remix-project.org/
[Hardhat]: https://hardhat.org/



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/introduction-to-solidity-vid.md -->

---
title: Introduction
description: Learn about the Solidity programming language.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='808096815' title='Introduction to Solidity' />



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/deployment-in-remix.md -->

---
title: Deployment in Remix
description: Use Remix to deploy and interact with a contract.
hide_table_of_contents: false
---

Remix contains a simulation of the blockchain that allows you to easily and safely deploy and interact with contracts, for free.

---

## Objectives

By the end of this lesson you should be able to:

- Deploy and test the Storage.sol demo contract in Remix

---

## Deploy the `Storage` Contract

Deploying a contract is easy, but remember that if the contract doesn't compile, the deploy button will instead deploy the last good compiled version of your contract. Verify that you see a green checkmark on the icon for the _Compiler_ contract on the left side of the editor, then select the _Deploy & Run Transactions_ plugin.

If you've already deployed any contracts, press the trash can button to the right of the _Deployed Contracts_ label. Then, press the orange button to deploy the `Storage` contract.

![Deploy](../../assets/images/introduction-to-solidity/deploy-button.png)

### Contract Addresses

After your contract deploys, it will appear in the _Deployed_ contracts section as _STORAGE AT_ followed by an address. Addresses are used for both contracts and wallets in EVM-compatible blockchains and serve a similar purpose to an IP address. You can copy the address to see what it looks like. It's 20 characters of hexadecimal, similar to `0xd8b934580fcE35a11B58C6D73aDeE468a2833fa8`.

The address is what you will use to find your contract with tools such as _Etherscan_, or to connect to it with a front end.

However, when you deploy using the Remix VM simulation, it will only exist in your browser.

### Deployments and Test Accounts

The result of any transactions, including deployments, will appear in the Remix terminal. Click the chevron next to the blue _Debug_ button to expand the log.

![Expand](../../assets/images/introduction-to-solidity/remix-deploy-chevron.png)

Doing so will show the full transaction log, which contains all of the details of the transaction, such as its amount, the address to and from, and the inputs and outputs provided to the transaction.

In this case, the sender (from) matches the first listed account in the panel, which has spent a small amount of simulated Ether to deploy the contract.

You can access a list of 15 test wallets here, each with 100 Ether to spend. Among other uses, you can use these accounts to compare behavior between wallets that are and are not the owner of a deployed contract.

### Interacting with the Contract

Click the chevron to expand your contract in the Deployed Contracts section of the left panel. You'll see two buttons, one for each `public` function in the `Storage` contract. Notice how the _Store_ button also has a field to pass a _uint256_, matching the parameter for `uint256 num`.

![Function Buttons](../../assets/images/introduction-to-solidity/remix-contract-buttons.png)

Let's click the retrieve button first. Before clicking, make a prediction: given that the `number` variable was instantiated without a value, what do you think the return will be?

Go ahead and click – the result will appear below the button as:

```text
0: uint256: 0
```

![Retrieve](../../assets/images/introduction-to-solidity/remix-retrieve.png)

Outputs from the EVM are in the form of an array, so in this case, the only return is in the 0th element and it is a `uint256` of 0. Were you expecting `undefined` or an error?

Unlike many languages, variables in Solidity have a [default value] if not assigned. For `uint` and `int`, that value is 0.

You can also review the results of your transaction in the console.

![Console](../../assets/images/introduction-to-solidity/remix-transaction-console.png)

The screenshot above is from a newer version of Remix than the video. Outputs are now often decoded for you!

### Storing and Retrieving a Value

Use the input to store and retrieve a value. Which costs more gas? Storing or retrieving? This isn't a trick question, but it is a bit nuanced. Both cost about 23500 gas, but there is only a gas cost for the retrieve function if it is called by another contract. Calling it from the web is free, because you're only reading data that is on the blockchain and are not asking the EVM to perform a computational task.

---

## Disabling Artifact Generation

Return to the _File Explorer_ by clicking the double document icon in the upper left. You should now see a folder called _artifacts_ that has been added to your project. This folder contains a number of build artifacts, such as the [_ABI_] for your contract, that will be useful to you later, but currently just cause clutter.

You can disable artifact generation by clicking the settings gear in the bottom left corner, then deselecting the first checkbox to _Generate contract metadata..._

![Settings](../../assets/images/introduction-to-solidity/remix-settings.png)

---

## Conclusion

Remix makes it easy to write, deploy, and test contracts. Contracts are deployed by a wallet address to their own address. These addresses are similar to how IP addresses work, in that they enable connections across the network. You can test deployed contracts directly in Remix and use the console to see detailed information about each transaction.

---

<!-- Reference Style Links -->

<!-- Add reference style links here.  These do not render on the page. -->

[default value]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html#scoping-and-declarations
[_ABI_]: https://docs.soliditylang.org/en/v0.8.13/abi-spec.html



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/introduction-to-remix.md -->

---
title: 'Introduction to Remix'
description: An introduction to the Remix online IDE.
hide_table_of_contents: false
---

# Introduction to Remix

In this lesson, you'll be introduced to an online Solidity IDE called Remix. You'll tour the workspace and explore a sample smart contract.

---

## Objectives

By the end of this lesson you should be able to:

- List the features, pros, and cons of using Remix as an IDE
- Deploy and test the Storage.sol demo contract in Remix

---

## Remix Window Overview

Begin by opening a browser window and navigating to [remix.ethereum.org]. Open the project you created and cleaned up at the end of the last reading, and open `1_Storage.sol`. The editor should be organized in a way that is familiar to you. It is divided into three areas:

- Editor Pane
- Terminal/Output
- Left Panel

### Editor Pane

The editor pane loads with the Remix home screen, which contains news, helpful links, and warnings about common scams. Double-click on `1_Storage.sol` to open it in the editor. You can close the home tab if you'd like.

![Remix Editor](../../assets/images/introduction-to-solidity/editor-pane.png)

You'll edit your code in the editor pane. It also has most of the features you're expecting, such as syntax and error highlighting. Note that in Remix, errors are not underlined. Instead, you'll see an❗to the left of the line number where the error is present.

At the top, you'll see a large green arrow similar to the _Run_ button in other editors. In Solidity, this compiles your code, but it does not run it because you must first deploy your code to the simulated blockchain.

### Terminal/Output

Below the editor pane, you'll find the terminal:

![Remix Terminal](../../assets/images/introduction-to-solidity/remix-terminal.png)

You'll primarily use this panel to observe transaction logs from your smart contracts. It's also one way to access Remix's very powerful debugging tools.

### Left Panel

As with many other editors, the left panel in Remix has a number of vertical tabs that allow you to switch between different tools and functions. You can explore the files in your current workspace, create and switch between workspaces, search your code, and access a number of plugins.

---

## Plugins

Most of the features in Remix are plugins and the ones you'll use the most are active by default. You can view and manage plugins by clicking the plug button in the lower-left corner, right above the settings gear. You can turn them off and on by clicking activate/deactivate, and some, such as the _Debug_ plugin will be automatically activated through other parts of the editor.

### Solidity Compiler

The first default plugin (after the search function) is the _Solidity Compiler_. Be sure to check the `Auto compile` option. Smart contracts are almost always very small files, so this shouldn't ever cause a performance problem while editing code.

The `Compile and Run script` button in this plugin is a little misleading. This is **not** how you will usually run your contract through testing. You can click the `I` button for more information on this feature.

Finally, if you have errors in your contracts, the complete text for each error will appear at the bottom of the pane. Try it out by introducing some typos to `1_Storage.sol`.

### Deploy & Run Transactions

The _Deploy & Run Transactions_ plugin is what you'll use to deploy your contracts and then interact with them. At the top are controls to select which virtual machine to use, mock user wallets with test Ether, and a drop-down menu to select the contract you wish to deploy and test.

Fix any errors you introduced to `1_Storage.sol` and then click the orange `Deploy` button. You'll see your contract appear below as _STORAGE AT \<address\>_.

:::caution

There are two common gotchas that can be very confusing when deploying contracts in Remix.

1. Each time you hit the Deploy button, a new copy of your contract is deployed but the previous deployments remain. Unless you are comparing or debugging between different versions of a contract, or deploying multiple contracts at once, you should click the `Trash` button to erase old deployments before deploying again.
1. If your code will not compile, **clicking the deploy button will not generate an error!** Instead, the last compiled version will be deployed. Visually check and confirm that there are no errors indicated by a number in a red circle on top of the Compiler plugin.

:::

---

## Conclusion

Remix is a robust editor with many features and one or two gotchas. It is an excellent tool to use at the beginning of your journey because you can jump right in and start writing code for smart contracts.

## See also

[Remix](https://remix.ethereum.org)

[remix.ethereum.org]: https://remix.ethereum.org



<!-- File: ../web/apps/base-docs/base-learn/docs/introduction-to-solidity/introduction-to-solidity-overview.md -->

---
title: 'Overview'
description: An overview of this module.
hide_table_of_contents: false
---

The course you are about to begin is designed to rapidly and thoroughly teach web3 concepts and language to web2 developers. It specifically highlights similarities and differences found in web3 vs. web2 and contains background information, guided coding practices, and independent exercises.

This program is **not** suitable for people who are new to programming in general. While the explanations are thorough, they often rely on an expectation that you are familiar with the underlying concepts. We will not teach you what arrays are and how they are used, but we will show you how they work in this environment.

## Prerequisites

Before these lessons, you should:

- Have several years of experience as a programmer in an object-oriented language
- Be familiar with the uses and properties of the Ethereum blockchain and the EVM
- Ideally, be familiar with at least one [curly-bracket] programming language

---

## Objectives

By the end of this module, you should be able to:

- **Introduction to Solidity**
  - Describe why languages like Solidity are used to write smart contracts
  - Relate an overview of the history (and pace of change) of Solidity and its strengths and weaknesses
  - Deploy and test the Storage.sol demo contract in Remix
- **Contracts and Basic Functions**
  - Construct a simple ""Hello World"" contract
  - Categorize basic data types
  - List the major differences between data types in Solidity as compared to other languages
  - Compare and contrast signed and unsigned integers
  - Write a pure function that accepts argument and returns a value
- **Deploying Smart Contracts to a Testnet**
  - Describe the uses and properties of the Ethereum testnet
  - Compare and contrast Ropsten, Rinkeby, Goerli, and Sepolia
  - Deploy a contract to the Sepolia testnet and interact with it in Etherscan
- **Control Structures**
  - Control code flow with if, else, while, and for
  - List the unique constraints for control flow in Solidity
- **Storage in Solidity**
  - Diagram how a contract's data is stored on the blockchain (Contract -> Blockchain)
  - Order variable declarations to use storage efficiently
  - Diagram how variables in a contract are stored (Variable -> Contract)
- **Arrays in Solidity**
  - Construct then store and retrieve values in storage and memory arrays
  - Describe the difference between storage and memory arrays
  - Diagram how arrays are stored
  - Write a function that can return a filtered subset of an array
- **The Mapping Type**
  - Construct a Map (dictionary) data type
  - Diagram the storage of the Mapping data type
  - Recall that assignment of the Map data type is not as flexible as for other data types/in other languages
  - Restrict function calls with the `msg.sender` global variable
  - Recall that there is no collision protection in the EVM and why this (probably) ok
- **Advanced Functions**
  - Describe how pure and view functions are different than functions that modify storage
  - Categorize functions as public, private, internal, or external based on their usage
  - Use modifiers to efficiently add functionality to multiple functions
  - Utilize require to write a function that can only be used when a variable is set to 'True'
- **Structs**
  - Construct a struct (user-defined type) that contains several different data types
  - Declare members of the struct to maximize storage efficiency
  - Describe constraints related to assignment of structs depending on the types they contain
- **Inheritance**
  - Write a smart contract that inherits from another contract
- **Imports**
  - Import and use code from another file
- **Errors**
  - Debug common solidity errors including execution reverted, out of gas, stack overflow, value overflow/underflow, index out of range, and so on
- **New Keyword**
  - Write a contract that creates a new contract with the new keyword

---

[curly-bracket]: https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Curly-bracket_languages



<!-- File: ../web/apps/base-docs/base-learn/docs/events/hardhat-events-sbs.md -->

---
title: Events
description: Events in Solidity
hide_table_of_contents: false
---

In this article, you'll learn how events work in Solidity by reviewing some practical examples and common use cases of events.

:::caution

This tutorial has been moved as part of a reorganization! It assumes you are using Hardhat. Everything in this lesson will work with minor adjustments if you are working in Foundry or Remix.

:::

---

## Objectives

By the end of this lesson, you should be able to:

- Write and trigger an event
- List common uses of events
- Understand events vs. smart contract storage

---

## Overview

Understanding how Solidity events work is important in the world of smart contract development. Events provide a powerful way to create event-driven applications on the blockchain. They allow you to notify external parties, such as off-chain applications, user interfaces, and any entity that wants to listen for events of a particular contract.

In this tutorial, you'll learn how to declare, trigger, and utilize events, gaining the knowledge necessary to enhance the functionality and user experience of your decentralized applications.

## What are events?

From the official solidity documentation, [events] are:

> _...an abstraction on top of the EVM’s logging functionality. Applications can subscribe and listen to these events through the RPC interface of an Ethereum client._

> _...when you call them, they cause the arguments to be stored in the transaction’s log – a special data structure in the blockchain. These logs are associated with the address of the contract that emitted them, are incorporated into the blockchain, and stay there as long as a block is accessible (forever as of now, but this might change in the future)._

In other words, events are an abstraction that allow you to store a transaction's log information in the blockchain.

## Your first solidity event

Start by creating a first event in the `Lock.sol` contract that's included by default in Hardhat.

The event is called `Created` and includes the address of the creator and the amount that was sent during the creation of the smart contract. Then, `emit` the event in the constructor:

```solidity
emit Created(msg.sender, msg.value);
```

The contract is:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract Lock {
    uint public unlockTime;
    address payable public owner;

    event Created(address owner, uint amount);

    constructor(uint _unlockTime) payable {
        require(
            block.timestamp < _unlockTime,
            "Unlock time should be in the future"
        );

        unlockTime = _unlockTime;
        owner = payable(msg.sender);

        emit Created(msg.sender, msg.value);
    }
}
```

Events can be defined at the file level or as inheritable members of contracts (including interfaces). You can also define the event in an interface as:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

interface ILock {
    event Created(address owner, uint amount);
}

contract Lock is ILock {
    uint public unlockTime;
    address payable public owner;

    constructor(uint _unlockTime) payable {
        require(
            block.timestamp < _unlockTime,
            "Unlock time should be in the future"
        );

        unlockTime = _unlockTime;
        owner = payable(msg.sender);

        emit Created(msg.sender, msg.value);
    }
}
```

You can test the event by simplifying the original test file with the following code:

```solidity
import {
  time,
} from "@nomicfoundation/hardhat-toolbox/network-helpers";
import { ethers } from "hardhat";

describe("Lock tests", function () {
  describe("Deployment", function () {
    it("Should set the right unlockTime", async function () {
      const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
      const ONE_GWEI = 1_000_000_000;

      const lockedAmount = ONE_GWEI;
      const unlockTime = (await time.latest()) + ONE_YEAR_IN_SECS;

      // Contracts are deployed using the first signer/account by default
      const [owner] = await ethers.getSigners();

      // But we do it explicit by using the owner signer
      const LockFactory = await ethers.getContractFactory("Lock", owner);
      const lock = await LockFactory.deploy(unlockTime, { value: lockedAmount });

      const hash = await lock.deploymentTransaction()?.hash
      const receipt = await ethers.provider.getTransactionReceipt(hash as string)

      console.log("Sender Address", owner.address)
      console.log("Receipt.logs", receipt?.logs)

      const defaultDecoder = ethers.AbiCoder.defaultAbiCoder()
      const decodedData = defaultDecoder.decode(['address', 'uint256'], receipt?.logs[0].data as string)
      console.log("decodedData", decodedData)
    });
  });
});
```

Notice that the previous code is logging the sender address and the logs coming from the transaction receipt. You are also decoding the `receipts.logs[0].data` field that contains the information emitted by the event but not in a human-readable way, since it is encoded. For that reason, you can use `AbiCoder` to decode the raw data.

By running `npx hardhat test`, you should be able to see the following:

```solidity
  Lock tests
    Deployment
Sender Address 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
Receipt.logs [
  Log {
    provider: HardhatEthersProvider {
      _hardhatProvider: [LazyInitializationProviderAdapter],
      _networkName: 'hardhat',
      _blockListeners: [],
      _transactionHashListeners: Map(0) {},
      _eventListeners: []
    },
    transactionHash: '0xad4ff104036f23096ea5ed165bff1c3e1bc0f53e375080f84bce4cc108c28cee',
    blockHash: '0xb2117cfd2aa8493a451670acb0ce14228b06d17bf545cd7efad6791aeac83c05',
    blockNumber: 1,
    removed: undefined,
    address: '0x5FbDB2315678afecb367f032d93F642f64180aa3',
    data: '0x000000000000000000000000f39fd6e51aad88f6f4ce6ab8827279cfffb92266000000000000000000000000000000000000000000000000000000003b9aca00',
    topics: [
      '0x0ce3610e89a4bb9ec9359763f99110ed52a4abaea0b62028a1637e242ca2768b'
    ],
    index: 0,
    transactionIndex: 0
  }
]
decodedData Result(2) [ '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266', 1000000000n ]
      ✔ Should set the right unlockTime (1008ms)
```

Notice the value `f39fd6e51aad88f6f4ce6ab8827279cfffb92266` is encoded in the property data, which is the address of the sender.

## Event topics

Another important feature is that events can be indexed by adding the indexed attribute to the event declaration.

For example, if you modify the interface with:

```solidity
interface ILock {
    event Created(address indexed owner, uint amount);
}
```

Then, if you run `npx hardhat test` again, an error may occur because the decoding assumes that the data field contains an `address` and a `uint256`. But by adding the indexed attribute, you are instructing that the events will be added to a special data structure known as "topics". Topics have some limitations, since the maximum indexed attributes can be up to three parameters and a topic can only hold a single word (32 bytes).

You then need to modify the decoding line in the test file with the following:

```solidity
const decodedData = defaultDecoder.decode(['uint256'], receipt?.logs[0].data as string)
```

Then, you should be able to see the receipt as:

```solidity
 Lock tests
    Deployment
Sender Address 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
Receipt.logs [
  Log {
    provider: HardhatEthersProvider {
      _hardhatProvider: [LazyInitializationProviderAdapter],
      _networkName: 'hardhat',
      _blockListeners: [],
      _transactionHashListeners: Map(0) {},
      _eventListeners: []
    },
    transactionHash: '0x0fd52fd72bca26879474d3e512fb812489111a6654473fd288c6e8ec0432e09d',
    blockHash: '0x138f74df5637315099d31aedf5bf643cf95c2bb7ae923c21fcd7f0075cb55324',
    blockNumber: 1,
    removed: undefined,
    address: '0x5FbDB2315678afecb367f032d93F642f64180aa3',
    data: '0x000000000000000000000000000000000000000000000000000000003b9aca00',
    topics: [
      '0x0ce3610e89a4bb9ec9359763f99110ed52a4abaea0b62028a1637e242ca2768b',
      '0x000000000000000000000000f39fd6e51aad88f6f4ce6ab8827279cfffb92266'
    ],
    index: 0,
    transactionIndex: 0
  }
]
decodedData Result(1) [ 1000000000n ]
      ✔ Should set the right unlockTime (994ms)
```

Notice the topics property, which now contains the address of the sender: `f39fd6e51aad88f6f4ce6ab8827279cfffb92266`.

## Common uses of events

Solidity events have several common use cases, which are described in the following sections.

### User notifications

Events can be used to notify users or external systems about certain contract actions.

### Logging

Events are primarily used to log significant changes within the contract, providing a transparent and verifiable history of what has occurred.

### Historical state reconstruction

Events can be valuable for recreating the historical state of a contract. By capturing and analyzing emitted event logs, you can reconstruct past states, offering a transparent and auditable history of the contract's actions and changes.

### Debugging and monitoring

Events are essential for debugging and monitoring contract behavior, as they provide a way to observe what's happening on the blockchain.

The ability to use events to recreate historical states provides an important auditing and transparency feature, allowing users and external parties to verify the contract's history and actions. While not a common use, it's a powerful capability that can be particularly useful in certain contexts.

## Events vs. smart contract storage

Although it is possible to rely on events to fully recreate the state of a particular contract, there are a few other options to consider.

Existing services such as [The Graph] allow you to index and create GraphQL endpoints for your smart contracts and generate entities based on custom logic. However, you must pay for that service since you are adding an intermediate layer to your application. This has the following benefits, such as:

- the ability to simply query one particular endpoint to get all the information you need
- your users will pay less gas costs due to the minimization of storage usage in your contract

But storing all of the information within the smart contract and relying fully on it to access data can create more complexity, since not all of the data is directly query-able. The benefits of this approach include:

- your application requires only the smart contract address to access all of the required data
- there are fewer dependencies involved, which makes this approach more crypto native in the sense that everything is in the blockchain (but, storing all the data in the blockchain will cause higher gas costs)

As a smart contract developer, you must evaluate which options work best for you.

## Conclusion

In this lesson, you've learned the basics of Solidity events and their importance in Ethereum smart contract development. You now understand how to declare and trigger events, a few of their common use cases, and the difference between events and smart contract storage.

Now that you have a solid grasp of events and their versatile applications, you can leverage them to build more sophisticated and interactive smart contracts that meet your specific needs, all while being mindful of the cost considerations.

---

## See also

[events]: https://docs.soliditylang.org/en/latest/contracts.html#events
[The Graph]: https://thegraph.com/



<!-- File: ../web/apps/base-docs/base-learn/docs/new-keyword/creating-a-new-contract-vid.md -->

---
title: Creating a `new` Contract
description: Use the `new` keyword to create a contract that can create contracts.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='823513272' title='Creating a `new` Contract' />



<!-- File: ../web/apps/base-docs/base-learn/docs/new-keyword/new-keyword-sbs.md -->

---
title: The New Keyword
description: Learn to create a contract that creates other contracts.
hide_table_of_contents: false
---

You've seen the `new` keyword and used it to instantiate `memory` arrays with a size based on a variable. You can also use it to write a contract that [creates other contracts].

---

## Objectives

By the end of this lesson you should be able to:

- Write a contract that creates a new contract with the new keyword

---

## Creating a Simple Contract Factory

A contract factory is a contract that creates other contracts. To start, let's create and interact with a very simple one. Create a new project in Remix and add a file called `ContractFactory.sol`.

### Adding the Template

Imagine you want to create a contract that can store its owner's name and compliment them upon request. You can create this contract fairly easily.

<details>

<summary>Reveal code</summary>

```solidity
contract Complimenter {
    string public name;

    constructor(string memory _name) {
        name = _name;
    }

    function compliment() public view returns(string memory) {
        return string.concat("You look great today, ", name);
    }
}
```

</details>

<br/>

Deploy and test.

### Creating a Factory

The `Complimenter` contract is a huge success! People love how it makes them feel and you've got customers banging on the doors and windows. Awesome!

The only problem is that it takes time and effort to manually deploy a new version of the contract for each customer. Luckily, there's a way to write a contract that will act as a self-service portal for your customers.

Start by adding a contract called `ComplimenterFactory`. The Remix interface makes things easier if you leave the factory in the same file as `Complimenter`.

Add a function called `CreateComplimenter` that is public, accepts a `string` called `_name`, and returns an `address`.

Creating a new contract is simple: `new Complimenter(_name)`

You can also save the return from that instantiation into a variable. This reference can be used to call public functions in the deployed contract, and can be cast to an address. We can use it to get an easy reference to find the copies made by the factory. The end result should look similar to:

<details>

<summary>Reveal code</summary>

```solidity
contract ComplimenterFactory {
    function CreateComplimenter(string memory _name) public returns (address) {
        Complimenter newContract = new Complimenter(_name);
        return address(newContract);
    }
}
```

</details>

<br/>

### Testing

Clear the environment if you haven't already, then start by deploying `ComplimenterFactory`. You've been working hard and deserve nice things, so call `CreateComplimenter` with your name.

In the terminal, the _decoded output_ will be the address of the new contract.

```text
{
	"0": "address: 0x9e0BC6DB02E5aF99b8868f0b732eb45c956B92dD"
}
```

Copy **only** the address.

Switch the _CONTRACT_ to be deployed to `Complimenter`, then paste the address you copied in the field next to the _At Address_ button which is below the _Deploy_ button.

![At address button](../../assets/images/new-keyword/at-address.png)

Click _At Address_ and the instance of `Complimenter` should appear below `ComplimenterFactory`. Test to confirm it works, then try deploying more instances with the factory.

![Deployed](../../assets/images/new-keyword/deployed.png)

:::tip

If the deployed contract appears, but is instead a broken copy of the factory, it's because you didn't change the contract in the _CONTRACT_ dropdown above the deploy button.

Remix is trying to interact with `Complimenter` using the _ABI_ from the factory contract, which won't work.

:::

---

## Conclusion

In this lesson, you learned how to deploy contracts from another contract by using the `new` keyword. You also learned that you look great today!

---

[creates other contracts]: https://docs.soliditylang.org/en/v0.8.17/control-structures.html?#creating-contracts-via-new



<!-- File: ../web/apps/base-docs/base-learn/docs/new-keyword/new-keyword-exercise.md -->

---
title: New Exercise
description: Exercise - Demonstrate your knowledge of the `new` keyword.
hide_table_of_contents: false
---

For this exercise, we're challenging you to build a solution requiring you to use a number of the concepts you've learned so far. Have fun and enjoy!

---

## Contracts

Build a contract that can deploy copies of an address book contract on demand, which allows users to add, remove, and view their contacts.

You'll need to develop two contracts for this exercise and import **at least** one additional contract.

## Imported Contracts

Review the [Ownable] contract from OpenZeppelin. You'll need to use it to solve this exercise.

You may wish to use another familiar contract to help with this challenge.

## AddressBook

Create an `Ownable` contract called `AddressBook`. In it include:

- A `struct` called `Contact` with properties for:
  - `id`
  - `firstName`
  - `lastName`
  - a `uint` array of `phoneNumbers`
- Additional storage for `contacts`
- Any other necessary state variables

It should include the following functions:

### Add Contact

The `addContact` function should be usable only by the owner of the contract. It should take in the necessary arguments to add a given contact's information to `contacts`.

### Delete Contact

The `deleteContact` function should be usable only by the owner and should delete the contact under the supplied `_id` number.

If the `_id` is not found, it should revert with an error called `ContactNotFound` with the supplied id number.

### Get Contact

The `getContact` function returns the contact information of the supplied `_id` number. It reverts with `ContactNotFound` if the contact isn't present.

:::tip Question

For bonus points (that only you will know about), explain why we can't just use the automatically generated getter for `contacts`?

:::

### Get All Contacts

The `getAllContacts` function returns an array with all of the user's current, non-deleted contacts.

:::caution

You shouldn't use `onlyOwner` for the two _get_ functions. Doing so won't prevent a third party from accessing the information, because all information on the blockchain is public. However, it may give the mistaken impression that information is hidden, which could lead to a security incident.

:::

## AddressBookFactory

The `AddressBookFactory` contains one function, `deploy`. It creates an instance of `AddressBook` and assigns the caller as the owner of that instance. It then returns the `address` of the newly-created contract.

---

## Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={12} />

[Ownable]: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol



<!-- File: ../web/apps/base-docs/base-learn/docs/help-on-discord.md -->

---
title: Get Help on Discord
description: Discover how to get help with Base Learn on Discord.
hide_table_of_contents: false
image: /img/base-learn-open-graph.png
---

Need help?

Whether you're confused about something weird in Solidity, having trouble getting through the frontend material, or just stuck on an exercise - we're here to help!

First, join the [Base Discord].

Then, get help from the community, Based Advocates, and the authors of the program in the [Base Learn] channel!

[Base Discord]: https://base.org/discord
[Base Learn Channel]: https://discord.com/channels/1067165013397213286/1108389436644917328



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-forking/hardhat-forking.md -->

---
title: Hardhat Forking
description: Learn how to fork
hide_table_of_contents: false
---

In this article, you'll learn how to fork smart contracts in Ethereum mainnet using Hardhat.

---

## Objectives

By the end of this lesson, you should be able to:

- Use Hardhat Network to create a local fork of mainnet and deploy a contract to it
- Utilize Hardhat forking features to configure the fork for several use cases

---

## Overview

Hardhat forking is a powerful feature that allows developers to create a local replica or fork of the Ethereum network or any other EVM-compatible Blockchain. By using this feature, you can develop smart contracts that rely on smart contracts that are already deployed to a particular network.

You will create a BalanceReader.sol contract that reads the USDC balance of a particular holder.

In order to achieve that, you need to:

- Create the BalanceReader.sol contract
- Configure Hardhat to support forking
- Create a test for the BalanceReader.sol contract

Hardhat forking also has other capabilities like:

- hardhat_impersonateAccount (useful to impersonate an account and others)
- hardhat_stopImpersonatingAccount
- hardhat_setNonce
- hardhat_setBalance
- hardhat_setCode
- hardhat_setStorageAt

Those won't be covered in this guide, however it's recommended to explore them a bit more in the following link:

- https://hardhat.org/hardhat-network/guides/mainnet-forking.html

## Creating the Balance Reader contract

The BalanceReader contract is created as follows:

```tsx
pragma solidity 0.8.9;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BalanceReader {
    function getERC20BalanceOf(address _account, address _tokenAddress)
        external
        view
        returns (uint256)
    {
        // we create an instance only using the interface and the address
        return IERC20(_tokenAddress).balanceOf(_account);
    }
}
```

You simply pass the address of an account and the address of a token, then you get and return the balance.

You will need to install @openzeppelin by running:

```bash
npm install @openzeppelin/contracts
```

Then, check that everything is working correctly by running:

```bash
npx hardhat compile
```

You should get:

```
Generating typings for: 2 artifacts in dir: typechain-types for target: ethers-v6
Successfully generated 18 typings!
Compiled 2 Solidity files successfully
```

## Configuring Hardhat to support forking

By default, Hardhat uses a network called `hardhat`. You must change its default configuration by going to the `hardhat.config.ts` file and include the following in the network:

```json
hardhat: {
    forking: {
        url: `https://eth-mainnet.g.alchemy.com/v2/${process.env.ALCHEMY_MAINNET_KEY ?? ""}`,
        enabled: true
    }
},
```

Be aware that you need to have an `ALCHEMY_MAINNET_KEY` in your .env file. You can get one directly from [Alchemy](https://www.alchemy.com/).

Also notice that forking is enabled by specifying `enabled: true`, however this value can be changed via environment variables.

## Creating a test for the BalanceReader.sol contract

Create a test file in the test folder called `BalanceReader.ts` and include the following:

```tsx
import { Signer } from 'ethers';
import { ethers } from 'hardhat';

import { BalanceReader, BalanceReader__factory } from '../typechain-types';

describe('BalanceReader tests', () => {
  let instance: BalanceReader;
  let accounts: Signer[];

  // Configure the addresses we can to check balances for
  const USDC_MAINNET_ADDRESS = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'; // https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
  const ARBITRUM_ONE_GATEWAY = '0xcEe284F754E854890e311e3280b767F80797180d';
  const USDC_DECIMALS = 6;

  it('gets arbitrum gateway balance', async () => {
    // We get signers as in a normal test
    accounts = await ethers.getSigners();
    const factory = new BalanceReader__factory(accounts[0]);

    // We deploy the contract to our local test environment
    instance = await factory.deploy();

    // Our contract will be able to check the balances of the mainnet deployed contracts and address
    const balance = await instance.getERC20BalanceOf(ARBITRUM_ONE_GATEWAY, USDC_MAINNET_ADDRESS);
    const balanceAsString = ethers.formatUnits(balance, USDC_DECIMALS);

    console.log(
      'The USDC Balance of Arbitrum Gateway is $',
      Number(balanceAsString).toLocaleString(),
    );
  });
});
```

In this example, the [USDC address](https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48) is used and since USDC is an ERC-20 token, you can explore the token holders of that particular token directly in Etherscan:

![Hardhat forking](../../assets/images/hardhat-forking/hardhat-forking.png)

Or, visit https://etherscan.io/token/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#balances, where you can see, at the time or writing, Arbitrum ONE Gateway is the top token holder.

Then, run the following command:

```bash
npx hardhat test ./test/BalanceReader.ts
```

You should get:

```
BalanceReader tests
The USDC Balance of Arbitrum Gateway is $ 1,116,923,836.506
    ✔ gets arbitrum gateway balance (4345ms)

  1 passing (4s)
```

## Conclusion

In this lesson, you've learned how to use hardhat forking capabilities to test smart contracts. You learned how contracts can interact with already-deployed contracts in an easy way.

---

## See also

[Solidity Docs]: https://docs.soliditylang.org/en/v0.8.17/
[Remix Project]: https://remix-project.org/
[Hardhat Deploy]: https://github.com/wighawag/hardhat-deploy
[Hardhat Forking]: https://hardhat.org/hardhat-network/docs/guides/forking-other-networks



<!-- File: ../web/apps/base-docs/base-learn/docs/hardhat-forking/mainnet-forking-vid.md -->

---
title: Forking Mainnet
description: Create a copy of the mainnet to run advanced tests.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='844047412' title='Mainnet Forking' />



<!-- File: ../web/apps/base-docs/base-learn/docs/deployment-to-testnet/deployment-to-base-sepolia-sbs.md -->

---
title: Deployment to Base Sepolia
description: Deploy your smart contract to a test network.
hide_table_of_contents: false
---

Remix contains a simulation of a blockchain that you can use to rapidly deploy and test your contracts. This simulation only exists within your browser so you can't share it with others, use external tools, or a front end to interact with it. However, you can also deploy to a variety of testnets from within Remix. Doing so will allow you to share your contract with others, at the cost of making it public.

---

## Objectives

By the end of this lesson you should be able to:

- Deploy a contract to the Base Sepolia testnet and interact with it in [BaseScan]

---

## Prepare for Deployment

Testnets operate in a similar, **but not exactly the same** manner as the main networks they shadow. You need a wallet with the appropriate token to interact with them by deploying a new contract or calling functions in a deployed contract.

### Set Up a Wallet

If you already have a wallet set up **exclusively for development**, you can skip to the next section. Otherwise, now is the time to jump in!

:::danger

It is very dangerous to use a wallet with valuable assets for development. You could easily write code with a bug that transfers the wrong amount of the wrong token to the wrong address. Transactions cannot be reversed once sent!

Be safe and use separate wallets for separate purposes.

:::

First, add the [Coinbase] or [Metamask] wallet to your browser, and then [set up] a new wallet. As a developer, you need to be doubly careful about the security of your wallet! Many apps grant special powers to the wallet address that is the owner of the contract, such as allowing the withdrawal of all the Ether that customers have paid to the contract or changing critical settings.

Once you've completed the wallet setup, enable developer settings and turn on testnets ([Coinbase Settings], [Metamask Settings]).

### Add Base Sepolia to your Wallet

Use the [faucet] to add Base Sepolia ETH to your wallet. You can also ask Base personnel on Discord or other social media for some!

### Get Testnet Ether

Testnet tokens have no real value, but the supply is not unlimited. You can use a faucet to get a small amount of Sepolia Ether to pay gas fees for testing. Most faucets allow you to ask for a small amount each day, and some won't send you more if your balance is too high.

You can find many faucets by searching, and it's good to keep a few bookmarked because they have a tendency to go down from time to time. Faucet providers are constantly combating bad actors and sometimes need to disable their faucets while doing so.

You can also access the [faucets on the web].

Once you have testnet Base Sepolia Ether, you can view your balance under the _Testnets_ tab in the Coinbase wallet or by selecting the testnet from the network dropdown in Metamask. Sadly, it's not actually worth the amount listed!

![Coinbase Balance](../../assets/images/deployment-to-testnet/balance.png)

---

## Deploying to Testnet

Once you have testnet Ether, you can deploy your BasicMath contract!

### Selecting the Environment

Open the _Deploy & Run Transactions_ tab. Under _Environment_, select _Injected Provider_. It will list _Coinbase_, _Metamask_, or any other wallet you have activated here.

![Environment](../../assets/images/deployment-to-testnet/select-provider.png)

If that option is not available, you can add it by choosing `Customize this list...`

![Add Injected Wallet](../../assets/images/deployment-to-testnet/add-injected-provider.png)

The first time you do this, your wallet will ask you to confirm that you want to connect this app (Remix) to your wallet.

Once you are connected, you'll see the name of the network below the _Environment_ dropdown.

![Connected](../../assets/images/deployment-to-testnet/remix-base-goerli-connected.png)

For Base Sepolia, you should see `Custom (84532) network`. The old network, Goerli, was `84531`. If you don't see the correct network, change the active network in your wallet.

### Deploy the Contract

Click the orange _Deploy_ button. Because it costs gas to deploy a contract, you'll be asked to review and confirm a transaction.

![Confirm](../../assets/images/deployment-to-testnet/base-confirm-transaction.png)

:::danger

Always carefully review all transactions, confirming the transaction cost, assets transferred, and network. As a developer, you'll get used to approving transactions regularly. Do the best you can to avoid getting into the habit of clicking _Confirm_ without reviewing the transaction carefully. If you feel pressured to _Confirm_ before you run out of time, it is almost certainly a scam.

:::

After you click the _Confirm_ button, return to Remix and wait for the transaction to deploy. Copy its address and navigate to [`sepolia.basescan.org`].

## Conclusion

You now have the power to put smart contracts on the blockchain! You've only deployed to a test network, but the process for real networks is exactly the same - just more expensive!

---

<!-- Add reference style links here.  These do not render on the page. -->

[`sepolia.basescan.org`]: https://sepolia.basescan.org/
[coinbase]: https://www.coinbase.com/wallet
[metamask]: https://metamask.io/
[faucet]: https://docs.base.org/tools/network-faucets
[set up]: 
[coinbase settings]: https://docs.cloud.coinbase.com/wallet-sdk/docs/developer-settings
[Metamask Settings]: https://support.metamask.io/hc/en-us/articles/13946422437147-How-to-view-testnets-in-MetaMask
[BaseScan]: https://sepolia.basescan.org/
[faucets on the web]: https://coinbase.com/faucets



<!-- File: ../web/apps/base-docs/base-learn/docs/deployment-to-testnet/test-networks.md -->

---
title: Test Networks
description: An overview of Base test networks
hide_table_of_contents: false
---

This article provides a concise overview of Base test networks, highlighting their advantages, potential challenges, and comparing some of the most popular testnets.

---

## Objectives:

By the end of this lesson you should be able to:

- Describe the uses and properties of the Base testnet
- Compare and contrast Ropsten, Rinkeby, Goerli, and Sepolia

---

## Why Testnets?

As you dive into the development of smart contracts and onchain apps on Base, mainnet, or other networks, you'll need a safe, controlled, and efficient environment for testing and experimentation. Test networks, or testnets, serve as essential tools for you to test your smart contracts before deploying them to the mainnet, minimizing the risk of failures or vulnerabilities in live applications.

By simulating the mainnet environment, testnets offer a realistic representation of real-world conditions, complete with network latency, gas fees, and other factors that impact the performance of smart contracts. This accurate representation enables you to identify potential issues, optimize your applications, and ensure the best possible user experience for your end-users. Moreover, testnets allow you to familiarize yourself with the Base ecosystem and gain valuable hands-on experience, making them indispensable tools for both seasoned developers and newcomers to the world of blockchain development.

![The Importance of Test Networks](../../assets/images/deployment-to-testnet/importance-of-testnets.png)

---

## The Advantages of Using Testnets

Testnets offer several key advantages to developers:

- **Real-time feedback:** Developers can quickly identify and fix errors or vulnerabilities in their smart contracts, ensuring robust and secure applications.

- **No cost or risk:** Testnets use "fake" ether, enabling developers to deploy and interact with smart contracts without incurring any financial cost or risk.

- **Easy accessibility:** Testnets are readily available for developers to join, allowing them to focus on development rather than infrastructure setup.

- **Stress testing:** Testnets provide a suitable environment to stress test the Ethereum network infrastructure under various conditions. By simulating high transaction volumes, developers can evaluate how their applications perform under load and optimize them accordingly.

- **Protocol upgrades and improvements:** Testnets allow developers to test new protocol updates, improvements, and potential forks before implementing them on the mainnet. This process helps identify any issues or incompatibilities and ensures a smoother transition to new features and optimizations.

---

## Challenges Associated with Testnets

While Ethereum testnets provide a valuable testing environment for developers, there are some challenges and limitations you should be aware of when using them:

- **Network congestion:** Just like the mainnet, testnets can experience periods of network congestion due to high transaction volumes or other factors. During these periods, developers might face slow transaction processing times, which could impact their testing process and potentially delay development.

- **Testnet instability:** Testnets may occasionally face downtime or network issues, which can disrupt the testing process. While these events are relatively rare, it's essential to be prepared for such occurrences and have a backup plan, such as switching to another testnet or using a local development environment.

- **Differences in network behavior:** Although testnets simulate the mainnet environment, there might be subtle differences in network behavior, gas fees, or transaction processing times between the two. These differences could potentially impact the performance of your smart contracts on the mainnet. It's crucial to be aware of these discrepancies and make any necessary adjustments before deploying your smart contracts to the mainnet.

- **Limited resources:** Testnet Ether is generally available for free through faucets, but these sources might have daily limits or other restrictions on the amount of testnet Ether that can be obtained. This limitation could affect your ability to perform extensive testing or carry out large-scale experiments on the testnet.

---

## Popular Testnets

Several well-known testnets have emerged over the years, each with its own set of features and benefits.

![Comparison of Test Networks](../../assets/images/deployment-to-testnet/testnet-comparison.png)

### L1 Testnets

- **Ropsten:** Ropsten played a significant role in Ethereum's history but was effectively deprecated by late 2022 when the Merge took place. The Merge marked the transition from proof-of-work to proof-of-stake consensus for the Ethereum mainnet. Ropsten's vulnerability to spam attacks and network instability made it unreliable for testing purposes.

- **Rinkeby:** Rinkeby offered better security than Ropsten and used a proof-of-authority consensus mechanism. However, it lacked decentralization and client diversity, which ultimately led to its decline in popularity. After the Merge, Rinkeby is no longer a recommended test network.

- **Goerli:** Launched in early 2019, Goerli initially utilized a multi-client proof-of-authority consensus model to improve stability and security. Following the Merge, it transitioned to a proof-of-stake consensus mechanism, maintaining its cross-client compatibility and making it an ideal choice for developers. As of January 2024, Goerli is being sunset in favor of Sepolia.

- **Sepolia:** As one of the two original primary testnets alongside Goerli, Sepolia is designed for developers seeking a lighter weight chain for faster synchronization and interaction. As of January 2024, it is now the preferred testnet and developers should migrate to using it.

### L2 Testnets

- **Base Sepolia:** As new Layer-2 networks emerged that settled on Ethereum's Layer-1, the need for testnets dedicated to these L2 networks also arose. For instance, the L2 network Base has its own testnet, known as Base Sepolia. This testnet settles on the Ethereum Sepolia L1 testnet, providing an environment for testing L2-specific features and smart contracts.

- **Optimism Sepolia:** Optimism, an Ethereum Layer-2 scaling solution utilizing Optimistic Rollups, has its own testnet called Optimism Sepolia. This testnet is also built on the Ethereum Sepolia L1 testnet and offers a testing environment for developers to experiment with Optimism's Layer-2 features, smart contracts, and apps.

---

## Conclusion

Ethereum and L2 testnets are essential for the safe and efficient development of smart contracts and apps, offering numerous advantages such as real-time feedback, cost-free testing, easy accessibility, stress testing, and protocol upgrade testing. Despite certain challenges associated with testnets, developers continue to rely on them for a robust testing environment. Among the various options, Sepolia has emerged as preferred choices for Ethereum developers due to enhanced security, stability, and strong community support. As the Ethereum ecosystem evolves, incorporating Layer-2 networks and other innovations, testnets will continue to play a crucial role in fostering blockchain development and contributing to the overall success and growth of the space.

---

## See Also

- [Networks](https://ethereum.org/en/developers/docs/networks/)
- [The History of Ethereum Testnets](https://consensys.net/blog/news/the-history-of-ethereum-testnets/)



<!-- File: ../web/apps/base-docs/base-learn/docs/deployment-to-testnet/overview-of-test-networks-vid.md -->

---
title: Overview of Test Networks
description: Learn about test networks.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='832071141' title='Overview of Test Networks' />



<!-- File: ../web/apps/base-docs/base-learn/docs/deployment-to-testnet/deployment-to-testnet-exercise.md -->

---
title: 'Deployment Exercise'
description: Exercise - Deploy your basic math contract and earn an NFT.
hide_table_of_contents: false
---

You've already built and deployed your [Basic Math] contract for this exercise. Now it's time to submit the address and earn an NFT pin to commemorate your accomplishment!

:::caution

We're currently in beta, so you'll only need to pay testnet funds to submit your contract, but this means you'll be getting a testnet NFT.

Stay tuned for updates!

:::

### Submit your Contract and Earn an NFT Badge! (BETA)

:::info

#### Hey, where'd my NFT go!?

[Testnets](../deployment-to-testnet/test-networks) are not permanent! Base Goerli [will soon be sunset](https://base.mirror.xyz/kkz1-KFdUwl0n23PdyBRtnFewvO48_m-fZNzPMJehM4), in favor of Base Sepolia.

As these are separate networks with separate data, your NFTs **will not** transfer over.

**Don't worry!** We've captured the addresses of all NFT owners on Base Goerli and will include them when we release the mechanism to transfer these NFTs to mainnet later this year! You can also redeploy on Sepolia and resubmit if you'd like!

:::

import CafeUnitTest from '../../../src/components/CafeUnitTest/index.jsx'

<CafeUnitTest nftNum={1}/>

---

[basic math]: ../contracts-and-basic-functions/basic-functions-exercise



<!-- File: ../web/apps/base-docs/base-learn/docs/deployment-to-testnet/contract-verification-sbs.md -->

---
title: Contract Verification
description: Verify your contract and interact with it.
hide_table_of_contents: false
---

Once your contract is deployed, you can verify it using a number of popular services. Doing so will let your users have confidence that your contract does what you claim, and will allow you to interact with it using a similar interface to what you used in Remix.

---

## Objectives

By the end of this lesson you should be able to:

- Verify a contract on the Base Sepolia testnet and interact with it in [BaseScan]

---

### Verify the Contract

Make sure you still have the address of the contract you deployed in the last article copied to the clipboard.

You can interact with your deployed contract using Remix, the same as before, but it's also possible to interact with it through BaseScan. Paste your address in the search field to find it.

On this page, you can review the balance, information about, and all the transactions that have ever occurred with your contract.

Click the _Contract_ tab in the main panel. At the top is a message asking you to _Verify and Publish_ your contract source code.

![Verify](../../assets/images/deployment-to-testnet/verify-and-publish.png)

Verifying your contract maps the names of your functions and variables to the compiled byte code, which makes it possible to interact with the contract using a human-readable interface.

Click the link. Your contract address is already entered.

Under _Please select Compiler Type_ choose \_Solidity (Single file)

For _Please Select Compiler Version_ select the version matching the `pragma` at the top of your source file. Our examples are currently using _v0.8.17+commit.8df45f5f_.

For _Please select Open Source License Type_ pick the license that matches what you selected for your contract as the `SPDX-License-Identifier`. Pick _None_ if you followed the Solidity-recommended practice of using `UNLICENSED`.

On the next page, copy and paste your source code in the window. Verify that you are not a robot, and click _Verify and Publish_. You should see a success message.

![Success](../../assets/images/deployment-to-testnet/compiler-debug-log.png)

Click the linked address to your contract to return to the contract page. You'll now see your code!

:::tip

If you have imports, you'll need to right-click on the name of the file and choose `Flatten`. Submit the newly generated `filename_flattened.sol` for verification.

:::

### Interact with the Contract

You can now interact with your contract using BaseScan. Click the _Read Contract_ button. Both of your functions will be listed here and can be tested using the web interface.

You won't have anything under _Write Contract_ because this contract doesn't have any functions that save data to state.

---

## Conclusion

With your contracts verified, you can interact with them using online tools and your users can be secure that your code does what you claim.

---

<!-- Add reference style links here.  These do not render on the page. -->

[`sepolia.basescan.org`]: https://sepolia.basescan.org/
[coinbase]: https://www.coinbase.com/wallet
[faucet]: https://docs.base.org/tools/network-faucets
[set up]: 
[coinbase settings]: https://docs.cloud.coinbase.com/wallet-sdk/docs/developer-settings
[BaseScan]: https://sepolia.basescan.org/
[faucets on the web]: https://coinbase.com/faucets



<!-- File: ../web/apps/base-docs/base-learn/docs/interfaces/testing-the-interface-vid.md -->

---
title: Testing the Interface
description: Start writing tests for interfaces.
hide_table_of_contents: false
---

:::caution

This tutorial has been moved as part of a reorganization! It assumes you are using Hardhat. Everything in this lesson will work with minor adjustments if you are working in Foundry or Remix.

:::

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='877160111' title='Testing the Interface' />



<!-- File: ../web/apps/base-docs/base-learn/docs/interfaces/calling-another-contract-vid.md -->

---
title: Calling Another Contract
description: Call the functions in another contract from your own contract.
hide_table_of_contents: false
---

:::caution

This tutorial has been moved as part of a reorganization! It assumes you are using Hardhat. Everything in this lesson will work with minor adjustments if you are working in Foundry or Remix.

:::

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='877157748' title='Calling Another Contract' />



<!-- File: ../web/apps/base-docs/base-learn/docs/interfaces/intro-to-interfaces-vid.md -->

---
title: Intro to Interfaces
description: Use interfaces to tell your contract how another works.
hide_table_of_contents: false
---

:::caution

This tutorial has been moved as part of a reorganization! It assumes you are using Hardhat. Everything in this lesson will work with minor adjustments if you are working in Foundry or Remix.

:::

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='877151475' title='Intro to Interfaces' />



<!-- File: ../web/apps/base-docs/base-learn/docs/interfaces/contract-to-contract-interaction.md -->

---
title: 'Contract to Contract Interaction'
description: Interact with other smart contracts
hide_table_of_contents: false
---

In this article, you'll learn how to interact with other smart contracts using interfaces and the `.call()` function, which allows you to interact with other smart contracts without using an interface.

:::caution

This tutorial has been moved as part of a reorganization! It assumes you are using Hardhat. Everything in this lesson will work with minor adjustments if you are working in Foundry or Remix.

:::

---

## Objectives

By the end of this lesson you should be able to:

- Use interfaces to allow a smart contract to call functions in another smart contract
- Use the `call()` function to interact with another contract without using an interface

---

## Overview

Interacting with external smart contracts is a very common task in the life of a smart contract developer. This includes interacting with contracts that are already deployed to a particular network.

Usually the creators of certain smart contracts document their functionality and expose their functions by providing interfaces that can be used to integrate those particular contracts into your own.

For instance, [Uniswap] provides documentation on how to interact with their smart contracts and also some packages to easily integrate their protocol.

In this example, you interact with the [Uniswap protocol] to create a custom pool for a custom pair of tokens.

Since the Uniswap protocol is already deployed, you will use [Hardhat forking] to test your contract.

You will also use the following two approaches in the example:

- Using interfaces
- Using the `.call()` function

## Interacting with deployed contracts using interfaces

You must first install the [Uniswap V3 core package] by running:

```bash
npm install @uniswap/v3-core
```

This package provides access to the Uniswap interfaces of the Core protocol.

Then, write a custom contract called `PoolCreator` with the following code:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Factory.sol";

contract PoolCreator {
    IUniswapV3Factory public uniswapFactory;

    constructor(address _factoryAddress) {
        uniswapFactory = IUniswapV3Factory(_factoryAddress);
    }

    function createPool(
        address tokenA,
        address tokenB,
        uint24 fee
    ) external returns (address poolAddress) {
        // Check if a pool with the given tokens and fee already exists
        poolAddress = uniswapFactory.getPool(tokenA, tokenB, fee);
        if (poolAddress == address(0)) {
            // If the pool doesn't exist, create a new one
            poolAddress = uniswapFactory.createPool(tokenA, tokenB, fee);
        }

        return poolAddress;
    }
}
```

Notice the following:

- You are importing a `IUniswapV3Factory` interface. The interface contains function declarations that include `getPool` and `createPool`:

```solidity
// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity >=0.5.0;

/// @title The interface for the Uniswap V3 Factory
/// @notice The Uniswap V3 Factory facilitates creation of Uniswap V3 pools and control over the protocol fees
interface IUniswapV3Factory {
    // ...
    // ...other function declarations

    /// @notice Returns the pool address for a given pair of tokens and a fee, or address 0 if it does not exist
    /// @dev tokenA and tokenB may be passed in either token0/token1 or token1/token0 order
    /// @param tokenA The contract address of either token0 or token1
    /// @param tokenB The contract address of the other token
    /// @param fee The fee collected upon every swap in the pool, denominated in hundredths of a bip
    /// @return pool The pool address
    function getPool(
        address tokenA,
        address tokenB,
        uint24 fee
    ) external view returns (address pool);

    /// @notice Creates a pool for the given two tokens and fee
    /// @param tokenA One of the two tokens in the desired pool
    /// @param tokenB The other of the two tokens in the desired pool
    /// @param fee The desired fee for the pool
    /// @dev tokenA and tokenB may be passed in either order: token0/token1 or token1/token0. tickSpacing is retrieved
    /// from the fee. The call will revert if the pool already exists, the fee is invalid, or the token arguments
    /// are invalid.
    /// @return pool The address of the newly created pool
    function createPool(
        address tokenA,
        address tokenB,
        uint24 fee
    ) external returns (address pool);
```

- The constructor receives the address of the pool factory and creates an instance of `IUniswapV3Factory`.
- The `createPool` function includes a validation to ensure the pool doesn't exist.
- The `createPool` function creates a new pool.

Then, create a test file called `PoolCreator.test.ts` with the following content:

```tsx
import { ethers } from 'hardhat';
import { HardhatEthersSigner } from '@nomicfoundation/hardhat-ethers/signers';

import { Token, Token__factory, PoolCreator, PoolCreator__factory } from '../typechain-types';

describe('PoolCreator tests', function () {
  const UNISWAP_FACTORY_ADDRESS = '0x1F98431c8aD98523631AE4a59f267346ea31F984';
  let tokenA: Token;
  let tokenB: Token;
  let poolCreator: PoolCreator;
  let owner: HardhatEthersSigner;

  before(async () => {
    const signers = await ethers.getSigners();
    owner = signers[0];
    tokenA = await new Token__factory().connect(owner).deploy('TokenA', 'TokenA');
    tokenB = await new Token__factory().connect(owner).deploy('TokenB', 'TokenB');
    poolCreator = await new PoolCreator__factory().connect(owner).deploy(UNISWAP_FACTORY_ADDRESS);
  });

  it('should create a pool', async () => {
    const contractAddress = await poolCreator.createPool.staticCall(tokenA, tokenB, 500);
    console.log('Contract Address', contractAddress);
    await poolCreator.createPool(tokenA, tokenB, 500);
  });
});
```

Notice the following:

- The address `0x1F98431c8aD98523631AE4a59f267346ea31F984` is the address of the Uniswap pool factory deployed to the Ethereum mainnet. This can be verified by looking at the Uniswap documentation that includes the [Deployment addresses of the contracts].
- You created two tokens, TokenA and TokenB, by using a `Token` contract.

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol){
        _mint(msg.sender, 1000 ether);
    }
}
```

Finally, run `npx hardhat test` and you should get a result similar to the following:

```
PoolCreator tests
Contract Address 0xa76662f79A5bC06e459d0a841190C7a4e093b04d
    ✔ should create a pool (1284ms)

  1 passing (5s)
```

## Interacting with external contracts using `.call()`

In the previous example, you accessed the Uniswap V3 Factory interface, however if you don't have access to the contract interface, you can use a special function called `call`.

Using `call`, you can call any contract as long as you know minimal information of the function signature. In this case, you should at least know that `createPool` requires three parameters:

- tokenA
- tokenB
- fee

The newly modified smart contract code looks as follows:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract PoolCreator {
    address public uniswapFactory;

    constructor(address _factoryAddress) {
        uniswapFactory = _factoryAddress;
    }

    function createPool(
        address tokenA,
        address tokenB,
        uint24 fee
    ) external returns (address poolAddress) {
         bytes memory payload = abi.encodeWithSignature(
            "createPool(address,address,uint24)",
            tokenA,
            tokenB,
            fee
        );

        (bool success, bytes memory data) = uniswapFactory.call(payload);
        require(success, "Uniswap factory call failed");

        // The pool address should be returned as the first 32 bytes of the data
        assembly {
            poolAddress := mload(add(data, 32))
        }

        require(poolAddress != address(0), "Pool creation failed");
        return poolAddress;
    }
}
```

Notice the following:

- By using `abi.encodeWithSignature`, you encode the payload required to make a smart contract call using the `.call()` function.
- Using `.call()` doesn't require you to import the interface.
- You load the pool address by using a special assembly operation called `mload`.

Try to run again the command `npx hardhat test` and you should expect the same result:

```
PoolCreator tests
Contract Address 0xa76662f79A5bC06e459d0a841190C7a4e093b04d
    ✔ should create a pool (1284ms)

  1 passing (5s)
```

## Conclusion

Interfaces or the `.call` function are two ways to interact with external contracts. Using interfaces provides several advantages, including type safety, code readability, and compiler error checking. When interacting with well-documented contracts like Uniswap, using interfaces is often the preferred and safest approach.

On the other hand, the `.call` function offers more flexibility but comes with greater responsibility. It allows developers to call functions on contracts even without prior knowledge of their interfaces. However, it lacks the type safety and error checking provided by interfaces, making it more error-prone.

---

[Uniswap]: https://docs.uniswap.org/contracts/v3/reference/core/UniswapV3Factory
[Uniswap protocol]: https://uniswap.org
[Hardhat forking]: https://hardhat.org/hardhat-network/docs/guides/forking-other-networks
[Uniswap V3 core package]: https://www.npmjs.com/package/@uniswap/v3-core
[Deployment addresses of the contracts]: https://docs.uniswap.org/contracts/v3/reference/deployments



<!-- File: ../web/apps/base-docs/base-learn/docs/etherscan/etherscan-sbs.md -->

---
title: Etherscan
description: Learn about Etherscan
hide_table_of_contents: false
---

In this article, you'll learn about Etherscan, a blockchain explorer to inspect the Blockchain state and activity.

---

## Objectives

By the end of this lesson, you should be able to:

- List some of the features of Etherscan
- Read data from the Bored Apes Yacht Club contract on Etherscan
- Write data to a contract using Etherscan.

---

## Overview

[Etherscan](https://etherscan.io) is a popular Blockchain explorer that works for several different networks. In it, you can explore the state and activity of a particular network.

![Etherscan](../../assets/images/etherscan/etherscan-user-interface.png)

You can explore:

- Blocks
- Transactions
- Smart contracts
- And more!

For instance, the following shows the details of a Block:

![Block](../../assets/images/etherscan/blocks.png)

Where you see information such as:

- Timestamp
- Transactions
- Block height
- And other details

There are many variations of Etherscan for different networks. For example:

- [Base](https://basescan.org)
- [Base Sepolia](https://sepolia.basescan.org)
- [Sepolia Etherscan](https://sepolia.etherscan.io)

## Reading data from smart contracts using Etherscan

One of the things you can do with Etherscan is interact with already-deployed contracts.

For example, if you want to read information from a famous contract such as [BAYC](https://etherscan.io/token/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d), you can simply go to Etherscan and explore the contract:

![BAYC](../../assets/images/etherscan/bayc.png)

You are able to see information such as:

- The ETH balance it holds
- The contract creator
- The transaction when it was created
- Latest transactions
- And the verified contract

In the **Contract** tab, you can see the full source code of BAYC:

![BAYC Verified](../../assets/images/etherscan/bayc-verified.png)

For a developer, verifying contracts is important since it gives transparency to your users. However, there are some risks because this means that bad actors can see the full source code and can try to exploit it.

In order to read the state of the BAYC, you can go to the main menu and select the option **Read Contract**:

![BAYC Read](../../assets/images/etherscan/bayc-read.png)

After you select that option, you are able to see all of the read functions of the contract.

You can also query who is the owner of the BAYC with id 150:

![BAYC Query](../../assets/images/etherscan/bayc-query.png)

## Writing data to smart contracts using Etherscan

In a similar fashion, you can read data from smart contracts using Etherscan. It is also possible to write data.

To write data, go to the **Write Contract** tab:

![Write Contract](../../assets/images/etherscan/bayc-write.png)

From there, connect your wallet by clicking the **Connect with web3** button.

After you connect, the following UI appears:

![Write BAYC Connected](../../assets/images/etherscan/bayc-write-connected.png)

You can then call the functions you wish to write to.

:::info

Be aware that you may need to have real Ethereum in case you want to write to a contract in Ethereum mainnet. Also, any logic that the smart contract defines will be respected. This means that if you try to write to a contract that verifies certain conditions during the transaction (e.g., a function where only the owner of the contract can write information), then you won't be able to execute the transaction if you are not the owner.

:::

## Conclusion

In this lesson, you've learned some of the main features of Etherscan, including interacting with already-deployed contracts such as BAYC in order to read and write data.

---

## See also

[Base]: https://basescan.org
[Base Sepolia]: https://sepolia.basescan.org
[Sepolia Etherscan]: https://sepolia.etherscan.io



<!-- File: ../web/apps/base-docs/base-learn/docs/etherscan/etherscan-vid.md -->

---
title: Etherscan
description: Use Etherscan to interact with your own and others's contracts.
hide_table_of_contents: false
---

import Video from '../../../src/components/VideoPlayer/index.jsx'

<Video videoId='841274068' title='Etherscan' />


