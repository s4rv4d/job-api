import { TokenSelectDropdown } from "@coinbase/onchainkit/token";
import TokenSelectorContainer from "../../components/TokenSelectorContainer.tsx";
import App from "../../components/App";

# `<TokenSelectDropdown />`

The `TokenSelectDropdown` component is a dropdown component that selects a token in a given list of tokens.

## Usage

```tsx twoslash
import { TokenSelectDropdown, Token } from "@coinbase/onchainkit/token";
const token = {} as Token;
const setToken = (token: Token) => {};
// ---cut-before---
<TokenSelectDropdown // [!code focus]
  token={token} // [!code focus]
  setToken={setToken} // [!code focus]
  options={[
    // [!code focus]
    {
      name: "Ethereum",
      address: "",
      symbol: "ETH",
      decimals: 18,
      image:
        "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
      chainId: 8453,
    },
    {
      name: "USDC",
      address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      symbol: "USDC",
      decimals: 6,
      image:
        "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
      chainId: 8453,
    },
    {
      name: "Dai",
      address: "0x50c5725949a6f0c72e6c4a641f24049a917db0cb",
      symbol: "DAI",
      decimals: 18,
      image:
        "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/d0/d7/d0d7784975771dbbac9a22c8c0c12928cc6f658cbcf2bbbf7c909f0fa2426dec-NmU4ZWViMDItOTQyYy00Yjk5LTkzODUtNGJlZmJiMTUxOTgy",
      chainId: 8453,
    },
  ]} // [!code focus]
/>; // [!code focus]
```

<App>
  <TokenSelectorContainer>
    {(token, setToken) => (
      <TokenSelectDropdown
        token={token}
        setToken={setToken}
        options={[
          {
            name: "Ethereum",
            address: "",
            symbol: "ETH",
            decimals: 18,
            image:
              "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
            chainId: 8453,
          },
          {
            name: "USDC",
            address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
            symbol: "USDC",
            decimals: 6,
            image:
              "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
            chainId: 8453,
          },
          {
            name: "Dai",
            address: "0x50c5725949a6f0c72e6c4a641f24049a917db0cb",
            symbol: "DAI",
            decimals: 18,
            image:
              "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/d0/d7/d0d7784975771dbbac9a22c8c0c12928cc6f658cbcf2bbbf7c909f0fa2426dec-NmU4ZWViMDItOTQyYy00Yjk5LTkzODUtNGJlZmJiMTUxOTgy",
            chainId: 8453,
          },
        ]}
      />
    )}
  </TokenSelectorContainer>
</App>

## Props

[`TokenSelectDropdownReact`](/token/types#tokenselectdropdownreact)

## CSS

```css
.ock-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #d1d5db #ffffff;
}
```

import { TokenRow } from "@coinbase/onchainkit/token";

# `<TokenRow />`

The `TokenRow` component displays token information in a row format to be used in list components.

## Usage

Token with an image url

```tsx twoslash
// @noErrors: 1109 - Expression expected
import { TokenRow } from '@coinbase/onchainkit/token';

const token = { ... };

<TokenRow token={token} />; // [!code focus]
```

<App>
  <TokenRow
    token={{
      address: "0x1234",
      chainId: 1,
      decimals: 18,
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
      name: "Ethereum",
      symbol: "ETH",
    }}
  />
</App>

Token without an image url

```tsx twoslash
// @noErrors: 1109 - Expression expected
import { TokenRow } from '@coinbase/onchainkit/token';

const token = { ... };

<TokenRow token={token} />; // [!code focus]
```

<App>
  <TokenRow
    token={{
      address: "0x1234",
      chainId: 1,
      decimals: 18,
      image: null,
      name: "Ethereum",
      symbol: "ETH",
    }}
    amount="1000.00234"
  />
</App>

Token with an amount

```tsx twoslash
// @noErrors: 1109 - Expression expected
import { TokenRow } from '@coinbase/onchainkit/token';

const token = { ... };

<TokenRow token={token} amount="1000" />; // [!code focus]
<TokenRow token={token} amount="0.00234567" />; // [!code focus]
```

<App>
  <TokenRow
    token={{
      address: "0x1234",
      chainId: 1,
      decimals: 18,
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
      name: "Ethereum",
      symbol: "ETH",
    }}
    amount="1000"
  />
  <TokenRow
    token={{
      address: "0x1234",
      chainId: 1,
      decimals: 18,
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
      name: "Ethereum",
      symbol: "ETH",
    }}
    amount="0.00234567"
  />
</App>

Variations with `hideImage` and `hideSymbol`

```tsx twoslash
// @noErrors: 1109 - Expression expected
import { TokenRow } from '@coinbase/onchainkit/token';

const token = { ... };

<TokenRow token={token} hideSymbol />; // [!code focus]
<TokenRow token={token} hideImage />; // [!code focus]
<TokenRow token={token} hideSymbol hideImage />; // [!code focus]
```

<App>
  <TokenRow
    token={{
      address: '0x1234',
      chainId: 1,
      decimals: 18,
      image:
        'https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png',
      name: 'Ethereum',
      symbol: 'ETH',
    }}
    hideSymbol
  />

{' '}

<TokenRow
token={{
    address: "0x1234",
    chainId: 1,
    decimals: 18,
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
    name: "Ethereum",
    symbol: "ETH",
  }}
hideImage
/>

<TokenRow
token={{
      address: '0x1234',
      chainId: 1,
      decimals: 18,
      image:
        'https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png',
      name: 'Ethereum',
      symbol: 'ETH',
    }}
hideSymbol
hideImage
/>
</App>

## Props

[`TokenRowReact`](/token/types#tokenrowreact)

-->

# `formatAmount`

The `formatAmount` utility is designed for consistent number formatting.

## Usage

:::code-group

```tsx twoslash [code]
import { formatAmount } from "@coinbase/onchainkit/token";

const amount = formatAmount("10000", { minimumFractionDigits: 2 });
```

```ts [return value]
"10,000.00"; // if in U.S. English locale

"10.000,00"; // if in EU country locale
```

:::

## Returns

`string` - The formatted amount.

## Parameters

[`FormatAmountOptions`](/token/types#formatamountoptions)

-

title: Token components & utilities Types
description: Glossary of Types in Token components & utilities.

---

# Types [Glossary of Types in Token components & utilities.]

## `FormatAmountOptions`

```ts
type FormatAmountOptions = {
  locale?: string; // User locale (default: browser locale)
  minimumFractionDigits?: number; // Minimum fraction digits for number decimals (default: 0)
  maximumFractionDigits?: number; // Maximum fraction digits for number decimals (default: 0)
};
```

## `FormatAmountResponse`

```ts
type FormatAmountResponse = string; // See Number.prototype.toLocaleString for more info
```

## `Token`

```ts
type Token = {
  address: Address; // The address of the token contract
  chainId: number; // The chain id of the token contract
  decimals: number; // The number of token decimals
  image: string | null; // A string url of the token logo
  name: string;
  symbol: string; // A ticker symbol or shorthand, up to 11 characters
};
```

## `TokenChipReact`

```ts
type TokenChipReact = {
  token: Token; // Rendered token
  onClick?: (token: Token) => void;
  className?: string;
};
```

## `TokenImageReact`

```ts
type TokenImageReact = {
  className?: string; // Optional additional CSS class to apply to the component
  size?: number; // size of the image in px (default: 24)
  token: Token;
};
```

## `TokenRowReact`

```ts
type TokenRowReact = {
  amount?: string; // Token amount
  className?: string;
  hideImage?: boolean;
  hideSymbol?: boolean;
  onClick?: (token: Token) => void; // Component on click handler
  token: Token; // Rendered token
};
```

## `TokenSearchReact`

```ts
type TokenSearchReact = {
  className?: string;
  delayMs?: number; // Debounce delay in milliseconds
  onChange: (value: string) => void; // Search callback function
};
```

## `TokenSelectButtonReact`

```ts
type TokenSelectDropdownReact = {
  className?: string;
  isOpen: boolean; // Determines carot icon direction
  onClick: () => void; // Button on click handler
  token?: Token; // Selected token
};
```

## `TokenSelectDropdownReact`

```ts
type TokenSelectDropdownReact = {
  options: Token[]; // List of tokens
  setToken: (token: Token) => void; // Token setter
  token?: Token; // Selected token
};
```

## `TokenSelectModalReact`

```ts
type TokenSelectModalReact = {
  options: Token[]; // List of tokens
  setToken: (token: Token) => void; // Token setter
  token?: Token; // Selected token
};
```

->

import { TokenImage } from "@coinbase/onchainkit/token";

# `<TokenImage />`

The `TokenImage` component is an image that crops token image to a circle with an adjustable size.

With `token` props has no image, render partial token symbol and deterministic dark color.

## Usage

`TokenImage` with an url

```tsx twoslash
// @noErrors: 2739 - missing properties from Token
import { TokenImage } from "@coinbase/onchainkit/token";
<div>
  // ---cut-before---
  <TokenImage
    token={{
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
    }}
    size={24}
  />
  <TokenImage
    token={{
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
    }}
    size={32}
  />
  // ---cut-after---
</div>;
```

<App>
  <div style={{ display: 'flex', gap: '8px', flexDirection: 'column'}}>
    <TokenImage
      token={{
        name: 'Ethereum',
        address: '',
        symbol: 'ETH',
        decimals: 18,
        image: 'https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png',
        chainId: 8453,
      }}
      size={24}
    />

    <TokenImage
      token={{
        name: 'Ethereum',
        address: '',
        symbol: 'ETH',
        decimals: 18,
        image: 'https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png',
        chainId: 8453,
      }}
      size={32}
    />

  </div>
</App>

`TokenImage` with null as src

```tsx twoslash
import { TokenImage } from "@coinbase/onchainkit/token";
<div>
  // ---cut-before---
  <TokenImage
    token={{
      name: "USDC",
      address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      symbol: "USDC",
      decimals: 6,
      image: null,
      chainId: 8453,
    }}
    size={24}
  />
  <TokenImage
    token={{
      name: "USDC",
      address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      symbol: "USDC",
      decimals: 6,
      image: null,
      chainId: 8453,
    }}
    size={32}
  />
  // ---cut-after---
</div>;
```

<App>
  <div style={{ display: 'flex', gap: '8px', flexDirection: 'column'}}>
    <TokenImage
      token={{
        name: 'USDC',
        address: '0x833589fcd6edb6e08f4c7c32d4f71b54bda02913',
        symbol: 'USDC',
        decimals: 6,
        image: null,
        blockchain: 'eth',
        chainId: 8453,
      }}
      size={24}
    />

    <TokenImage
      token={{
        name: 'USDC',
        address: '0x833589fcd6edb6e08f4c7c32d4f71b54bda02913',
        symbol: 'USDC',
        decimals: 6,
        image: null,
        blockchain: 'eth',
        chainId: 8453,
      }}
      size={32}
    />

  </div>
</App>

## Props

[`TokenImageReact`](/token/types#tokenselectorreact)

## CSS

```css
.ock-tokenimage {
  @apply overflow-hidden rounded-[50%];
}
```

-->

import { TokenSearch } from "@coinbase/onchainkit/token";

# `<TokenSearch />`

The `<TokenSearch />` is a search component with an optional debounce delay.

If you want to handle debounce delay outside of this component, set `delayMs` to `0`.

## Usage

Use [`getTokens`](/api/get-tokens) and `<TokenSearch />` combined to search the [Tokens](/token/types#token).

```tsx twoslash
// @noErrors: 7006 2322 1128 - 'value' implicitly has any type, Type GetTokensResponse is not assignable to type Token[]
import { useCallback } from 'react';
import { base } from 'viem/chains';
// ---cut-before---
import { OnchainKitProvider } from '@coinbase/onchainkit';
import { getTokens } from '@coinbase/onchainkit/api'; // [!code focus]
import { TokenSearch } from '@coinbase/onchainkit/token'; // [!code focus]
import type { Token } from '@coinbase/onchainkit/token'; // [!code focus]

...

// example of async onChange handler
const handleChange = useCallback((value: string) => {
  async function getData(value) {
    const tokens: Token[] = await getTokens({ search: value }); // [!code focus]
    // Do something with tokens here
  }
  getData(value);
}, []);

...

<OnchainKitProvider
  chain={base}
  apiKey="YOUR_API_KEY"
>
  <TokenSearch onChange={handleChange} delayMs={200} /> // [!code focus]
</OnchainKitProvider>
```

<App>
  <TokenSearch
    onChange={(value) => console.log("Search term:", value)}
    delayMs={200}
  />
</App>

## Props

[`TokenSearch`](/token/types#tokensearchreact)

>

import { TokenChip } from "@coinbase/onchainkit/token";

# `<TokenChip />`

The `TokenChip` component is a button that displays the token symbol.

## Usage

```tsx twoslash
// @noErrors: 2322 - type 'string' is not assignable to type 0x{string}
import { TokenChip } from "@coinbase/onchainkit/token";
import "@coinbase/onchainkit/styles.css";

const token = {
  address: "0x1234",
  chainId: 1,
  decimals: 18,
  image:
    "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  name: "Ethereum",
  symbol: "ETH",
};

<TokenChip token={token} />; // [!code focus]
```

<App>
  <TokenChip
    token={{
      address: "0x1234",
      chainId: 1,
      decimals: 18,
      image:
        "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
      name: "Ethereum",
      symbol: "ETH",
    }}
  />
</App>

## Props

[`TokenChipReact`](/token/types#tokenchipreact)

.mdx -->

---

title: <Transaction /> · OnchainKit
description: The `<Transaction />` components provide a high-level wrap around the entire transaction flow. It handles the transaction lifecycle, including gas estimation, fee sponsorship, and status updates.

---

import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
Transaction,
TransactionButton,
TransactionDefault,
TransactionSponsor,
TransactionStatus,
TransactionStatusAction,
TransactionStatusLabel,
TransactionToast,
TransactionToastAction,
TransactionToastIcon,
TransactionToastLabel,
} from "@coinbase/onchainkit/transaction";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import TransactionWrapper from "../../components/TransactionWrapper";

export const BASE_SEPOLIA_CHAIN_ID = 84532;
export const PAYMASTER_AND_BUNDLER_ENDPOINT = import.meta.env
.VITE_CDP_PAYMASTER_AND_BUNDLER_ENDPOINT;

# `<Transaction />`

The `<Transaction />` components provide a high-level wrap around the entire transaction flow.
It handles the transaction lifecycle, including gas estimation, fee sponsorship, and status updates.

Before using them, ensure you've completed all [Getting Started steps](/getting-started).

## Quick start

The `TransactionDefault` component is a simplified version of the `Transaction` component, designed to streamline the integration process for developers. Instead of manually defining each subcomponent and prop, developers can use this shorthand version which renders our suggested implementation of the component and includes the `TransactionButton` and `TransactionToast` components.

If you'd like more customization, follow the implementation guide for our `Swap` component below.

```tsx twoslash
// @noErrors: 2580 2304 - Cannot find name 'process', Cannot find name 'contracts'
import { TransactionDefault } from "@coinbase/onchainkit/transaction";
// ---cut-before---
// omitted for brevity
<TransactionDefault contracts={contracts} />;
```

<App>
  <TransactionWrapper>
    {({ address, contracts, onStatus }) => {
      const capabilities = {
        paymasterService: {
          url: PAYMASTER_AND_BUNDLER_ENDPOINT,
        },
      };
      if (address) {
        return (
          <TransactionDefault
            capabilities={capabilities}
            chainId={BASE_SEPOLIA_CHAIN_ID}
            contracts={contracts}
            onStatus={onStatus}
          />
        );
      } else {
        return (
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        );
      }
    }}
  </TransactionWrapper>
</App>

### Props

[`TransactionDefaultReact`](/transaction/types#transactiondefaultreact)

## Walkthrough

::::steps

### Add `contracts`

Execute one or multiple `contracts` using the Transaction component. Each `contract` should include:

- `address`: the contract address;
- `abi`: the contract's ABI;
- `functionName`: a function to extract from the ABI;
- `args`: arguments to pass to the function call.

:::code-group

```tsx twoslash [TransactionComponents.tsx]
// @noErrors: 2307 - cannot find module './contracts' or its corresponding type declarations
import { useCallback } from "react";
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  // [!code focus]
  Transaction, // [!code focus]
  TransactionButton,
  TransactionSponsor,
  TransactionStatus,
  TransactionStatusAction,
  TransactionStatusLabel,
} from "@coinbase/onchainkit/transaction"; // [!code focus]
import type { LifecycleStatus } from "@coinbase/onchainkit/transaction";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import { contracts } from "./contracts"; // [!code focus]
// ---cut-start---

const BASE_SEPOLIA_CHAIN_ID = 84532;
// ---cut-end---

export default function TransactionComponents() {
  const { address } = useAccount();

  const handleOnStatus = useCallback((status: LifecycleStatus) => {
    console.log("LifecycleStatus", status);
  }, []);

  return address ? (
    <Transaction // [!code focus]
      chainId={BASE_SEPOLIA_CHAIN_ID} // [!code focus]
      contracts={contracts} // [!code focus]
      onStatus={handleOnStatus}
    >
      {" "}
      // [!code focus]
      <TransactionButton />
      <TransactionSponsor />
      <TransactionStatus>
        <TransactionStatusLabel />
        <TransactionStatusAction />
      </TransactionStatus>
    </Transaction> // [!code focus]
  ) : (
    <Wallet>
      <ConnectWallet>
        <Avatar className="h-6 w-6" />
        <Name />
      </ConnectWallet>
    </Wallet>
  );
}
```

```ts twoslash [contracts.ts]
const clickContractAddress = "0x67c97D1FB8184F038592b2109F854dfb09C77C75";
const clickContractAbi = [
  {
    type: "function",
    name: "click",
    inputs: [],
    outputs: [],
    stateMutability: "nonpayable",
  },
] as const;

export const contracts = [
  {
    address: clickContractAddress,
    abi: clickContractAbi,
    functionName: "click",
    args: [],
  },
];
```

:::

<App>
  <TransactionWrapper>
    {({ address, contracts, onStatus }) => {
      const capabilities = {
        paymasterService: {
          url: PAYMASTER_AND_BUNDLER_ENDPOINT,
        },
      };
      if (address) {
        return (
          <Transaction
            capabilities={capabilities}
            chainId={BASE_SEPOLIA_CHAIN_ID}
            contracts={contracts}
            onStatus={onStatus}
          >
            <TransactionButton />
            <TransactionSponsor />
            <TransactionStatus>
              <TransactionStatusLabel />
              <TransactionStatusAction />
            </TransactionStatus>
          </Transaction>
        );
      } else {
        return (
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        );
      }
    }}
  </TransactionWrapper>
</App>

### Listen to `LifecycleStatus`

Take full control of your transactions data with the `LifecycleStatus` object via the `onStatus` prop.
This TypeScript object provides `statusName` and `statusData` to keep you informed.

```tsx twoslash
// @noErrors: 2307 - cannot find module './contracts' or its corresponding type declarations
import { useCallback } from "react";
import {
  Transaction,
  TransactionButton,
  TransactionSponsor,
  TransactionStatus,
  TransactionToast,
  TransactionToastIcon,
  TransactionToastLabel,
  TransactionToastAction,
} from "@coinbase/onchainkit/transaction";
import { contracts } from "./contracts";
// ---cut-before---
import type { LifecycleStatus } from "@coinbase/onchainkit/transaction"; // [!code focus]

// omitted for brevity

const handleOnStatus = useCallback((status: LifecycleStatus) => {
  // [!code focus]
  console.log("LifecycleStatus", status); // [!code focus]
}, []); // [!code focus]

// omitted for brevity

<Transaction // [!code focus]
  contracts={contracts}
  onStatus={handleOnStatus} // [!code focus]
>
  {" "}
  // [!code focus]
  <TransactionButton />
  <TransactionSponsor />
  <TransactionToast>
    <TransactionToastIcon />
    <TransactionToastLabel />
    <TransactionToastAction />
  </TransactionToast>
</Transaction>; // [!code focus]
```

The Lifecycle Status features seven states for the transaction experience.

```ts twoslash
import type { TransactionError } from "@coinbase/onchainkit/transaction";
import type { Address, TransactionReceipt } from "viem";
// ---cut-before---
type LifecycleStatus =
  | {
      statusName: "init";
      statusData: null;
    }
  | {
      statusName: "error";
      statusData: TransactionError;
    }
  | {
      statusName: "transactionIdle"; // initial status prior to the mutation function executing
      statusData: null;
    }
  | {
      statusName: "buildingTransaction"; // resolving calls or contracts promise
      statusData: null;
    }
  | {
      statusName: "transactionPending"; // if the mutation is currently executing
      statusData: null;
    }
  | {
      statusName: "transactionLegacyExecuted";
      statusData: {
        transactionHashList: Address[];
      };
    }
  | {
      statusName: "success"; // if the last mutation attempt was successful
      statusData: {
        transactionReceipts: TransactionReceipt[];
      };
    };
```

### Sponsor with Paymaster capabilities

To sponsor your transactions with Paymaster capabilities, provide the `paymasterService` object.

Obtain a Paymaster and Bundler endpoint from the [Coinbase Developer Platform](https://portal.cdp.coinbase.com/products/bundler-and-paymaster).

<img
  alt="OnchainKit Paymaster and Bundler endpoint"
  title="OnchainKit Paymaster and Bundler endpoint"
  src="/assets/onchainkit-components-paymaster-endpoint.png"
  width="702"
  loading="lazy"
/>

```tsx twoslash
// @noErrors: 2580 2304 2322 - Cannot find name 'process', Cannot find name 'contracts'
import {
  Transaction,
  TransactionButton,
  TransactionSponsor,
} from "@coinbase/onchainkit/transaction";
// ---cut-before---
// omitted for brevity
<Transaction
  capabilities={{
    // [!code focus]
    paymasterService: {
      // [!code focus]
      url: process.env.PAYMASTER_AND_BUNDLER_ENDPOINT, // [!code focus]
    }, // [!code focus]
  }} // [!code focus]
  contracts={contracts}
>
  <TransactionButton />
  <TransactionSponsor />
</Transaction>;
```

::::

### Using `calls` instead of `contracts`

In addition to the `contracts` prop, the `<Transaction />` component also accepts a `calls` prop. This provides an alternative way to construct transactions. When using `calls`, you should not pass anything for the `contracts` prop.

Using `calls` instead of `contracts` is a great way to bundle several operations into a single transaction for smart wallets. Externally Owned Accounts (EOAs) such as the Coinbase Wallet extension will execute each call one-at-a-time with a separate pop-up for each.

The `calls` prop is an array of `Call` objects, where each `Call` is defined as:

```tsx twoslash
// @noErrors: 2304 Cannot find name 'Hex'
type Call = {
  to: Hex;
  data?: Hex;
  value?: bigint;
};
```

- `to`: The address you are executing the call on
- `data`: The encoded function data to pass along in the call (optional)
- `value`: The amount of ether to send along with the call, denominated in wei (optional)

Here's an example of how to use the `calls` prop with the Transaction component:

```tsx twoslash
import {
  Transaction,
  TransactionButton,
} from "@coinbase/onchainkit/transaction";
import { encodeFunctionData, Hex } from "viem";
import { baseSepolia } from "wagmi/chains";

const clickContractAddress: Hex = "0x67c97D1FB8184F038592b2109F854dfb09C77C75";
const clickContractAbi = [
  {
    type: "function",
    name: "click",
    inputs: [],
    outputs: [],
    stateMutability: "nonpayable",
  },
] as const;

const encodedClickData = encodeFunctionData({
  abi: clickContractAbi,
  functionName: "click",
});

const calls = [
  {
    to: clickContractAddress,
    data: encodedClickData,
  },
];

export default function TransactionWithCalls() {
  return (
    <Transaction
      chainId={baseSepolia.id}
      calls={calls}
      onStatus={(status) => console.log("Transaction status:", status)}
    >
      <TransactionButton />
    </Transaction>
  );
}
```

In this example, we're creating a single call to the `click` function of our contract. The `encodeFunctionData` utility from `viem` is used to encode the function call data.

### Using calls or contracts with Promises

Calls or contracts also accepts asynchronous functions that are resolved on each button click. This can be useful if you're calling an API to retrieve transaction data.

These functions must resolve to `Calls[]` or `ContractFunctionParameters[]`.

In the example the calls data will be fetched from api.transaction.com when the user clicks the Transaction Button.

```tsx twoslash
// @noErrors: 2322
import {
  Transaction,
  TransactionButton,
} from "@coinbase/onchainkit/transaction";
import { baseSepolia } from "wagmi/chains";

// ---cut-before---

const callsCallback = async () => {
  // [!code focus]
  const res = await fetch("api.transaction.com/createTransaction"); // [!code focus]
  const callData = await res.json(); // [!code focus]
  return callData; // [!code focus]
}; // [!code focus]

export default function TransactionWithCalls() {
  return (
    <Transaction
      chainId={baseSepolia.id}
      calls={callsCallback} // [!code focus]
      onStatus={(status) => console.log("Transaction status:", status)}
    >
      <TransactionButton />
    </Transaction>
  );
}
```

## Components

<div className="flex flex-col max-w-[648px] gap-6">
  <img
    src="/assets/onchainkit-components-transaction-anatomy.png"
    alt="OnchainKit transaction anatomy component diagram"
    title="Visual breakdown of OnchainKit transaction components"
    width="648"
    loading="lazy"
  />
</div>

The components are designed to work together hierarchically. For each component, ensure the following:

- `<Transaction />` - Serves as the main container for all transaction-related components.
- `<TransactionButton />` - Handles the transaction initiation process.
- `<TransactionSponsor />` - Displays information about the sponsorship of transaction gas fees.
- `<TransactionStatus />` - Contains transaction status information and actions.
- `<TransactionStatusLabel />` - Displays the current status of the transaction.
- `<TransactionStatusAction />` - Provides additional actions based on the transaction status.
- `<TransactionToast />` - Displays a toast notification for the transaction status.
- `<TransactionToastIcon />` - Displays an icon in the transaction toast notification.
- `<TransactionToastLabel />` - Displays the label text in the transaction toast notification.
- `<TransactionToastAction />` - Provides additional actions within the transaction toast notification.

## Component types

- [`TransactionButtonReact`](/transaction/types#transactionbuttonreact)
- [`TransactionError`](/transaction/types#transactionerror)
- [`TransactionDefaultReact`](/transaction/types#transactiondefaultreact)
- [`TransactionReact`](/transaction/types#transactionreact)
- [`TransactionSponsorReact`](/transaction/types#transactionsponsorreact)
- [`TransactionStatusReact`](/transaction/types#transactionstatusreact)
- [`TransactionStatusActionReact`](/transaction/types#transactionstatusactionreact)
- [`TransactionStatusLabelReact`](/transaction/types#transactionstatuslabelreact)
- [`TransactionToastReact`](/transaction/types#transactiontoastreact)
- [`TransactionToastActionReact`](/transaction/types#transactiontoastactionreact)
- [`TransactionToastIconReact`](/transaction/types#transactiontoasticonreact)
- [`TransactionToastLabelReact`](/transaction/types#transactiontoastlabelreact)

->

---

title: Transaction components & utilities Types
description: Glossary of Types in Transaction components & utilities.

---

# Types [Glossary of Types in Transaction components & utilities.]

## `Call`

```ts
type Call = { to: Hex; data?: Hex; value?: bigint };
```

## `LifecycleStatus`

```ts
type LifecycleStatus =
  | {
      statusName: "init";
      statusData: null;
    }
  | {
      statusName: "error";
      statusData: TransactionError;
    }
  | {
      statusName: "transactionIdle"; // initial status prior to the mutation function executing
      statusData: null;
    }
  | {
      statusName: "buildingTransaction"; // resolving calls or contracts promise
      statusData: null;
    }
  | {
      statusName: "transactionPending"; // if the mutation is currently executing
      statusData: null;
    }
  | {
      statusName: "transactionLegacyExecuted";
      statusData: {
        transactionHashList: Address[];
      };
    }
  | {
      statusName: "success"; // if the last mutation attempt was successful
      statusData: {
        transactionReceipts: TransactionReceipt[];
      };
    };
```

## `TransactionButtonReact`

```ts
type TransactionButtonReact = {
  className?: string; // An optional CSS class name for styling the button component.
  disabled?: boolean; // A optional prop to disable the submit button
  text?: string; // An optional text to be displayed in the button component.
};
```

## `TransactionError`

```ts
type TransactionError = {
  code: string; // The error code representing the type of transaction error.
  error: string; // The error message providing details about the transaction error.
  message: string; // The error message providing details about the transaction error.
};
```

## `TransactionReact`

```ts
type TransactionReact = {
  calls?: Call[] | Promise<Call[]> | (() => Promise<Call[]>); // An array, Promise or callback that resolves to an array of calls to be made in the transaction. Mutually exclusive with the `contracts` prop.
  capabilities?: WalletCapabilities; // Capabilities that a wallet supports (e.g. paymasters, session keys, etc).
  chainId?: number; // The chainId for the transaction.
  children: ReactNode; // The child components to be rendered within the transaction component.
  className?: string; // An optional CSS class name for styling the component.
  contracts?:
    | ContractFunctionParameters[]
    | Promise<ContractFunctionParameters[]>
    | (() => Promise<ContractFunctionParameters[]>); // An array, Promise or callback that resolves to an array of contract function parameters for the transaction. Mutually exclusive with the `calls` prop.
  onError?: (e: TransactionError) => void; // An optional callback function that handles transaction errors.
  onStatus?: (lifecycleStatus: LifecycleStatus) => void; // An optional callback function that exposes the component lifecycle state
  onSuccess?: (response: TransactionResponse) => void; // An optional callback function that exposes the transaction receipts
};
```

## `TransactionDefaultReact`

```ts
export type TransactionDefaultReact = {
  disabled?: boolean;
} & Omit<TransactionReact, "children">;
```

## `TransactionResponse`

```ts
type TransactionResponse = {
  transactionReceipts: TransactionReceipt[]; // An array containing the transaction receipts
};
```

## `TransactionSponsorReact`

```ts
type TransactionSponsorReact = {
  className?: string; // An optional CSS class name for styling the sponsor component.
};
```

## `TransactionStatusReact`

```ts
type TransactionStatusReact = {
  children: ReactNode; // The child components to be rendered within the status component.
  className?: string; // An optional CSS class name for styling the status component.
};
```

## `TransactionStatusActionReact`

```ts
type TransactionStatusActionReact = {
  className?: string; // An optional CSS class name for styling.
};
```

## `TransactionStatusLabelReact`

```ts
type TransactionStatusLabelReact = {
  className?: string; // An optional CSS class name for styling.
};
```

## `TransactionToastReact`

```ts
type TransactionToastReact = {
  children: ReactNode; // The child components to be rendered within the toast component.
  className?: string; // An optional CSS class name for styling the toast component.
  durationMs?: number; // An optional value to customize time until toast disappears
  position?: "top-center" | "top-right" | "bottom-center" | "bottom-right"; // An optional position property to specify the toast's position on the screen.
};
```

## `TransactionToastActionReact`

```ts
type TransactionToastActionReact = {
  className?: string; // An optional CSS class name for styling.
};
```

## `TransactionToastIconReact`

```ts
type TransactionToastIconReact = {
  className?: string; // An optional CSS class name for styling.
};
```

## `TransactionToastLabelReact`

```ts
type TransactionToastLabelReact = {
  className?: string; // An optional CSS class name for styling.
};
```

## `WalletCapabilities`

```ts
type WalletCapabilities = {
  paymasterService?: PaymasterService;
};
```

title: Access Denied
description: Restricted Access to OnchainKit
content:
width: 100%
layout: landing
showOutline: false

---

<div className="flex justify-center p-4">
  <div className="text-center">
    <h1 className="text-3xl md:text-4xl">Access Restricted</h1>
    <p className="text-lg md:text-xl">
      You're not allowed to use OnchainKit from a restricted territory.
    </p>
  </div>
</div>

->

# `getName`

The `getName` utility is designed to retrieve a name from an onchain identity
provider for a specific address.

Consider the utility instead of the hook when you
use it with Next.js or any Node.js backend.

## Usage

Get ENS name from an address:

:::code-group

```tsx twoslash [code]
import { getName } from "@coinbase/onchainkit/identity";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const name = await getName({ address });
```

```ts [return value]
zizzamia.eth;
```

:::

Get Basename from an address:

:::code-group

```tsx twoslash [code]
import { getName } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const name = await getName({ address, chain: base });
```

```ts [return value]
zizzamia.base.eth;
```

:::

Get a sliced address when address does not have an ENS name:

:::code-group

```tsx twoslash [code]
import { getName } from "@coinbase/onchainkit/identity";

const address = "0x1234567890abcdef1234567890abcdef12345678";
const name = await getName({ address });
```

```ts [return value]
0x123...5678
```

:::

## Returns

[`Promise<GetNameReturnType>`](/identity/types#getnamereturntype)

## Parameters

[`GetName`](/identity/types#getname)

x -->

# `useAddress`

The `useAddress` hook is used to get an address from an onchain identity provider for a given name.

## Usage

```tsx twoslash
import { useAddress } from "@coinbase/onchainkit/identity";

const { data: address, isLoading } = useAddress({ name: "zizzamia.base.eth" });
```

## Returns

[`useQuery<Promise<GetAddressReturnType>>`](/identity/types#getaddressreturntype)

## Parameters

[`UseAddressOptions`](/identity/types#useaddressoptions)
[`UseQueryOptions`](/identity/types#usequeryoptions)

>

import { Address } from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";

# `<Address />`

The `Address` component is used to render shorten user account address.

## Usage

Sliced account address:

```tsx twoslash
import { Address } from "@coinbase/onchainkit/identity";
<Address address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" />; // [!code focus]
```

<App>
  <Address address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" />
</App>

### Display full address

Set `isSliced` to false, to display the full address:

```tsx twoslash
import { Address } from "@coinbase/onchainkit/identity";
<Address
  address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1"
  isSliced={false}
/>; // [!code focus]
```

<App>
  <Address
    address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1"
    isSliced={false}
  />
</App>

### Override styles

You can override component styles using `className`.

```tsx twoslash
import { Address } from "@coinbase/onchainkit/identity";
<Address
  className="bg-emerald-400 px-2 py-1 rounded" // [!code focus]
  address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1"
/>;
```

<App>
  <Address
    className="bg-emerald-400 px-2 py-1 rounded"
    address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1"
  />
</App>

## Props

[`AddressReact`](/identity/types#addressreact)

x -->

# `getAddress`

The `getAddress` utility is designed to retrieve an address from an onchain identity provider for a given name.

## Usage

Get ENS Name from mainnet chain

:::code-group

```tsx twoslash [code]
import { getAddress } from "@coinbase/onchainkit/identity";

const address = await getAddress({ name: "zizzamia.eth" });
```

```ts [return value]
0x02feeb0ade57b6adeede5a4eeea6cf8c21beb6b1;
```

:::

Get Basename from base chain

:::code-group

```tsx twoslash [code]
import { getAddress } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const address = await getAddress({ name: "zizzamia.base.eth", chain: base });
```

```ts [return value]
0x02feeb0ade57b6adeede5a4eeea6cf8c21beb6b1;
```

:::

## Returns

[`Promise<GetAddressReturnType>`](/identity/types#getaddressreturntype)

## Parameters

[`GetAddress`](/identity/types#getaddress)

-->

# `getAvatar`

The `getAvatar` utility is designed to retrieve an avatar image
URL from an onchain identity provider for a given name.

Consider the utility instead of the hook when you
use it with Next.js or any Node.js backend.

Supported providers:

- [Basenames](https://www.base.org/names)
- ENS

## Usage

Get Basename avatar:

:::code-group

```tsx twoslash [code]
import { getAvatar } from "@coinbase/onchainkit/identity";
import { base, mainnet } from "viem/chains";

const baseAvatar = await getAvatar({ ensName: "paulcramer.eth", chain: base });
```

```ts [return value]
https://zku9gdedgba48lmr.public.blob.vercel-storage.com/basenames/avatar/paul.base.eth/1722120524815/FWUzoZmJ_400x400-kWjr2gMvjNe9hHMs9Z9LxGVGIME3By.jpg
```

:::

Get ENS avatar:

:::code-group

```tsx twoslash [code]
import { getAvatar } from "@coinbase/onchainkit/identity";
import { mainnet } from "viem/chains";

const ensAvatar = await getAvatar({
  ensName: "paulcramer.eth",
  chain: mainnet,
});
```

```ts [return value]
https://euc.li/paulcramer.eth;
```

:::

## Returns

[`Promise<GetAvatarReturnType>`](/identity/types#getavatarreturntype)

-->

# `useAvatar`

The `useAvatar` hook is used to get avatar image url from an onchain identity
provider for a given name.

## Usage

```tsx twoslash
import { useAvatar } from "@coinbase/onchainkit/identity";

const { data: avatar, isLoading } = useAvatar({ ensName: "vitalik.eth" });
```

## Returns

[`useQuery<Promise<GetAddressReturnType>>`](/identity/types#getaddressreturntype)

## Parameters

[`UseAvatarOptions`](/identity/types#useavataroptions)
[`UseQueryOptions`](/identity/types#usequeryoptions)

import { base } from "viem/chains";
import { Avatar, Badge, Name, Identity } from "@coinbase/onchainkit/identity";

# `<Badge />`

Use `Badge` component along with [`Avatar`](/identity/avatar) or [`Name`](/identity/name) components to display user attestations attached to their account

## Usage

Badge with default colors:

:::code-group

```tsx twoslash [tsx]
import { Badge } from "@coinbase/onchainkit/identity";
<Badge className="badge" />; // [!code focus]
```

```css [css]
.badge {
  background: #4f46e5;
  path {
    fill: #f9fafb;
  }
}
```

:::

<App>
  <Badge className="badge" />
</App>

Badge with custom colors:

```tsx twoslash
import { Badge } from "@coinbase/onchainkit/identity";
<Badge className="bg-blue-400 border-white" />; // [!code focus]
```

<App>
  <Badge className="bg-blue-400 border-white" />
</App>

## Props

[`BadgeReact`](/identity/types#BadgeReact)

## Badge on `<Name />` and `<Avatar />`

Badge with [`<Name />`](/identity/name), best used when [`<Name />`](/identity/name) are displayed alongside [`<Avatar />`](/identity/avatar) components.

In both examples we use the Coinbase [Verified Account](https://base.easscan.org/schema/view/0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9) schema ID to show the Coinbase verified badge on the Name and Avatar components.

```tsx twoslash
import { base } from "viem/chains";
import { Badge, Name, Identity } from "@coinbase/onchainkit/identity";

const address = "0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9";
const COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID =
  "0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9";

<Identity
  className="bg-transparent"
  schemaId={COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID} // [!code focus]
  address={address} // [!code focus]
>
  <Name address={address}>
    {" "}
    // [!code focus]
    <Badge /> // [!code focus]
  </Name>{" "}
  // [!code focus]
</Identity>;
```

<App>
  <Identity
    className="bg-transparent"
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
  >
    <Name address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9">
      <Badge />
    </Name>
  </Identity>
</App>

Badge with [`<Avatar />`](/identity/avatar), best used when [`<Avatar />`](/identity/avatar) is not paired with any labels.

```tsx twoslash
import { base } from "viem/chains";
import { Avatar, Badge, Identity } from "@coinbase/onchainkit/identity";

const address = "0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9";
const COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID =
  "0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9";

<Identity
  className="bg-transparent"
  schemaId={COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID} // [!code focus]
>
  <Avatar address={address}>
    {" "}
    // [!code focus]
    <Badge /> // [!code focus]
  </Avatar>{" "}
  // [!code focus]
</Identity>;
```

<App>
  <Identity
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
    className="bg-transparent"
  >
    <Avatar address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9">
      <Badge />
    </Avatar>
  </Identity>
</App>

->

# `useName`

The `useName` hook is used to get name from an onchain identity provider
for a given address.

## Usage

Get ENS name from an address:

:::code-group

```tsx twoslash [code]
import { useName } from "@coinbase/onchainkit/identity";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const { data: name, isLoading } = await useName({ address });
```

```ts [return value]
{ data: 'zizzamia.eth', isLoading: false }
```

:::

Get Basename from an address:

:::code-group

```tsx twoslash [code]
import { useName } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const { data: name, isLoading } = await useName({ address, chain: base });
```

```ts [return value]
{ data: 'zizzamia.base.eth', isLoading: false }
```

:::

## Returns

[`useQuery<Promise<GetAddressReturnType>>`](/identity/types#getaddressreturntype)

## Parameters

[`UseNameOptions`](/identity/types#usenameoptions)
[`UseQueryOptions`](/identity/types#usequeryoptions)

import { Badge, Name, Identity } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

# `<Name />`

The `Name` component is used to display ENS or [Basenames](https://www.base.org/names) associated with Ethereum addresses.

## Usage

Address with an ENS:

```tsx twoslash
import { Name } from "@coinbase/onchainkit/identity";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
<Name address={address} />; // [!code focus]
```

<App>
  <Name address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" />
</App>

Address with a Basename:

```tsx twoslash
import { Name } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains"; // [!code focus]

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
<Name address={address} chain={base} />; // [!code focus]
```

<App>
  <Name address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" chain={base} />
</App>

### Override styles

You can override component styles using `className`.

```tsx twoslash
import { Name } from "@coinbase/onchainkit/identity";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
<Name
  address={address}
  className="bg-emerald-400 px-2 py-1 rounded" // [!code focus]
/>;
```

<App>
  <Name
    className="bg-emerald-400 px-2 py-1 rounded"
    address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1"
  />
</App>

### Add attestation badge

Show attestation on ENV name with [`Badge`](/identity/badge) component.

Use [`OnchainKitProvider`](/config/onchainkit-provider) or [`Identity`](/identity/identity) component with the `schemaId` prop.

```tsx twoslash
import { Badge, Name, Identity } from "@coinbase/onchainkit/identity"; // [!code focus]

const address = "0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9";
<Identity
  address={address}
  schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9" // [!code focus]
>
  <Name>
    {" "}
    // [!code focus]
    <Badge /> // [!code focus]
  </Name>{" "}
  // [!code focus]
</Identity>;
```

<App>
  <Identity
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    className="bg-transparent"
  >
    <Name>
      <Badge />
    </Name>
  </Identity>
</App>

## Props

[`NameReact`](/identity/types#namereact)

---

title: Identity components & utilities Types
description: Glossary of Types in Identity components & utilities.

---

# Types [Glossary of Types in Identity components & utilities.]

## `AddressReact`

```ts
type AddressReact = {
  address?: Address | null; // The Ethereum address to render.
  className?: string; // Optional className override for top span element.
  isSliced?: boolean; // Determines if the displayed address should be sliced.
};
```

## `Attestation`

```ts
type Attestation = {
  attester: Address; // the attester who created the attestation.
  decodedDataJson: string; // The attestation data decoded to JSON.
  expirationTime: number; // The Unix timestamp when the attestation expires (0 for no expiration).
  id: string; // The unique identifier of the attestation.
  recipient: Address; // The Ethereum address of the recipient of the attestation.
  revocationTime: number; // The Unix timestamp when the attestation was revoked, if applicable.
  revoked: boolean; // A boolean indicating whether the attestation is revocable or not.
  schemaId: EASSchemaUid; // The schema identifier associated with the attestation.
  time: number; // The Unix timestamp when the attestation was created.
};
```

## `AvatarReact`

```ts
type AvatarReact = {
  address?: Address | null; // The Ethereum address to fetch the avatar for.
  chain?: Chain; // Optional chain for domain resolution
  className?: string; // Optional className override for top div element.
  loadingComponent?: JSX.Element; // Optional custom component to display while the avatar data is loading.
  defaultComponent?: JSX.Element; // Optional custom component to display when no ENS name or avatar is available.
  children?: ReactNode; // Optional attestation by passing Badge component as its children
} & ImgHTMLAttributes<HTMLImageElement>; // Optional additional image attributes to apply to the avatar.
```

## `BadgeReact`

```ts
type BadgeReact = {
  className?: string; // Optional className override for top span element.
};
```

## `BaseMainnetName`

```ts
export type BaseMainnetName = `${string}.base.eth`;
```

## `Basename`

```ts
type Basename = BaseMainnetName | BaseSepoliaName;
```

## `BaseSepoliaName`

```ts
type BaseSepoliaName = `${string}.basetest.eth`;
```

## `EASSchemaUid`

```ts
type EASSchemaUid = `0x${string}`;
```

## `EASChainDefinition`

```ts
type EASChainDefinition = {
  easGraphqlAPI: string; // EAS GraphQL API endpoint
  id: number; // blockchain source id
  schemaUids: EASSchemaUid[]; // Array of EAS Schema UIDs
};
```

## `EthBalanceReact`

```ts
type EthBalanceReact = {
  address?: Address;
  className?: string;
};
```

## `GetAddress`

```ts
type GetAddress = {
  name: string | Basename;
  chain?: Chain;
};
```

## `GetAddressReturnType`

```ts
type GetAddressReturnType = Address | null;
```

## `GetAttestationsOptions`

```ts
type GetAttestationsOptions = {
  schemas?: EASSchemaUid[];
  revoked?: boolean;
  expirationTime?: number;
  limit?: number;
};
```

## `GetAvatar`

```ts
type GetAvatar = {
  chain?: Chain; // Optional chain for domain resolution
  ensName: string; // The ENS name to fetch the avatar for.
};
```

## `GetAvatarReturnType`

```ts
type GetAvatarReturnType = string | null;
```

## `GetName`

```ts
type GetName = {
  address: Address;
  chain?: Chain;
};
```

## `GetNameReturnType`

```ts
type GetNameReturnType = string | null;
```

## `IdentityContextType`

```ts
type IdentityContextType = {
  address: Address; // The Ethereum address to fetch the avatar and name for.
  schemaId?: Address | null; // The Ethereum address of the schema to use for EAS attestation.
};
```

## `IdentityReact`

```ts
type IdentityReact = {
  address?: Address; // The Ethereum address to fetch the avatar and name for.
  chain?: Chain; // Optional chain for domain resolution
  children: ReactNode;
  className?: string; // Optional className override for top div element.
  schemaId?: Address | null; // The Ethereum address of the schema to use for EAS attestation.
  hasCopyAddressOnClick?: boolean;
};
```

## `NameReact`

```ts
type NameReact = {
  address?: Address | null; // Ethereum address to be displayed.
  children?: ReactNode; // Optional attestation by passing Badge component as its children
  chain?: Chain; // Optional chain for domain resolution
  className?: string; // Optional className override for top span element.
} & HTMLAttributes<HTMLSpanElement>; // Optional additional span attributes to apply to the name.
```

## `UseAddressOptions`

```ts
type UseAddressOptions = {
  name: string | Basename; // The ENS or Basename for which the Ethereum address is to be fetched
  chain?: Chain; // Optional chain for domain resolution
};
```

## `UseAvatarOptions`

```ts
type UseAvatarOptions = {
  ensName: string;
  chain?: Chain; // Optional chain for domain resolution
};
```

## `UseQueryOptions`

```ts
type UseQueryOptions = {
  enabled?: boolean;
  cacheTime?: number;
};
```

## `UseNameOptions`

```ts
type UseNameOptions = {
  address: Address; // The Ethereum address for which the ENS name is to be fetched.
  chain?: Chain; // Optional chain for domain resolution
};
```

->

---

title: <Identity /> · OnchainKit
description: Identity components & utilities

---

import {
Address,
Avatar,
Identity,
Name,
Badge,
} from "@coinbase/onchainkit/identity";

# `<Identity />`

`Identity` is a React context provider and arranges identity components.

## Usage

Show user avatar, name with attestation and address:

```tsx twoslash
import {
  Avatar,
  Identity,
  Name,
  Badge,
  Address,
} from "@coinbase/onchainkit/identity";

<Identity // [!code focus]
  address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9" // [!code focus]
  schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9" // [!code focus]
>
  {" "}
  // [!code focus]
  <Avatar /> // [!code focus]
  <Name>
    {" "}
    // [!code focus]
    <Badge /> // [!code focus]
  </Name> // [!code focus]
  <Address /> // [!code focus]
</Identity>; // [!code focus]
```

<App>
  <Identity
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
  >
    <Avatar />
    <Name>
      <Badge />
    </Name>
    <Address />
  </Identity>
</App>

Modify any styles with `className` prop.

```tsx twoslash
import {
  Avatar,
  Identity,
  Name,
  Badge,
  Address,
} from "@coinbase/onchainkit/identity";

<Identity
  address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
  schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
>
  <Avatar>
    <Badge className="bg-error" /> // [!code focus]
  </Avatar>
  <Name className="text-orange-600" /> // [!code focus]
  <Address className="text-gray-500 font-bold" /> // [!code focus]
</Identity>;
```

<App>
  <Identity
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
  >
    <Avatar>
      <Badge className="bg-error" />
    </Avatar>
    <Name className="text-orange-600" />
    <Address className="text-gray-500 font-bold" />
  </Identity>
</App>

Choose which identity components to render:

```tsx twoslash
import {
  Avatar,
  Identity,
  Name,
  Badge,
  Address,
} from "@coinbase/onchainkit/identity";
// ---cut-start---
<div>
  // ---cut-end---
  <Identity address="0x838..." schemaId="0xf8b...">
    <Avatar /> // [!code focus]
    <Name>
      {" "}
      // [!code focus]
      <Badge /> // [!code focus]
    </Name> // [!code focus]
  </Identity>
  <Identity address="0x838..." schemaId="0xf8b...">
    <Name>
      {" "}
      // [!code focus]
      <Badge /> // [!code focus]
    </Name>{" "}
    // [!code focus]
    <Address /> // [!code focus]
  </Identity>
  // ---cut-after---
</div>;
```

<App>
  <Identity
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
  >
    <Avatar />
    <Name>
      <Badge />
    </Name>
  </Identity>
  <Identity
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
    className="mt-2"
  >
    <Name>
      <Badge />
    </Name>
    <Address />
  </Identity>
</App>

## Props

[`IdentityReact`](/identity/types#identityreact)

ns.mdx -->

# `getAttestations`

The `getAttestations` function fetches attestations for a specified address
and blockchain in Ethereum Attestation Service (EAS). It allows optional filtering
based on schema IDs, revocation status, expiration time, and the number of attestations to return.

In the example, we use the Coinbase [Verified Account](https://base.easscan.org/schema/view/0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9) schema ID.

## Usage

:::code-group

```tsx twoslash [code]
// @noErrors: 2345 - Argument of type string is not assignable to 0x{string}
import { getAttestations } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID =
  "0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9";

const address = "0x1234567890abcdef1234567890abcdef12345678";
const attestationsOptions = {
  schemas: [COINBASE_VERIFIED_ACCOUNT_SCHEMA_ID],
};

const attestations = await getAttestations(address, base, attestationsOptions);
```

```ts [return value]
const attestations = [
  {
    attester: "0x357458739F90461b99789350868CD7CF330Dd7EE",
    decodedDataJson:
      '[{"name":"verifiedAccount","type":"bool","signature":"bool verifiedAccount","value":{"name":"verifiedAccount","type":"bool","value":true}}]',
    expirationTime: 0,
    id: "0xf1fdb9d102f4b7c1d3b729fc10fea68596301c831913468f3f77f2d631486e12",
    recipient: "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1",
    revocationTime: 0,
    revoked: false,
    schemaId:
      "0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9",
    time: 1704433703,
    timeCreated: 1704433705,
    txid: "0x71e21910fd44c2b75b143cf71318507b60d09c5f3caf848109974dd397de9f37",
  },
];
```

:::

## Returns

[`Promise<Attestation[]>`](/identity/types#attestation)

## Parameters

### Address

```ts
type Address = `0x${string}`; // The address for which attestations are being queried.
```

### Chain

```ts
type Chain = {
  // The blockchain of interest.
  id: string;
  name: string;
  network: string;
  chainId: number;
  nativeCurrency: {
    name: string;
    symbol: string;
    decimals: number;
  };
  rpcUrls: string[];
  blockExplorerUrls: string[];
};
```

### GetAttestationsOptions

[`GetAttestationsOptions`](/identity/types#geteasttestationsoptions)

import { Avatar, Badge, Identity } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

# `<Avatar />`

The `Avatar` component is used to display ENS or [Basenames](https://www.base.org/names) avatar associated with Ethereum addresses.
When an avatar is not available, it defaults to blue color avatar.

## Usage

Address with an ENS avatar:

```tsx twoslash
import { Avatar } from "@coinbase/onchainkit/identity";
<Avatar address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9" />; // [!code focus]
```

<App>
  <Avatar address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9" />
</App>

Address without an ENS or Basenames avatar defaults to a plain avatar:

```tsx twoslash
import { Avatar } from "@coinbase/onchainkit/identity";
<Avatar address="0x1234567890abcdef1234567890abcdef12345678" />; // [!code focus]
```

<App>
  <Avatar address="0x1234567890abcdef1234567890abcdef12345678" />
</App>

Address with a Basename avatar:

```tsx twoslash
import { Avatar } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains"; // [!code focus]

<Avatar address="0x4bEf0221d6F7Dd0C969fe46a4e9b339a84F52FDF" chain={base} />; // [!code focus]
```

<App>
  <Avatar address="0x4bEf0221d6F7Dd0C969fe46a4e9b339a84F52FDF" chain={base} />
</App>

Override styles via `className` prop:

```tsx twoslash
import { Avatar } from "@coinbase/onchainkit/identity";
<Avatar // [!code focus]
  className="bg-white rounded-full" // [!code focus]
  address="0x1234567890abcdef1234567890abcdef12345678"
/>; // [!code focus]
```

<App>
  <Avatar
    className="bg-white rounded-full"
    address="0x1234567890abcdef1234567890abcdef12345678"
  />
</App>
Use `defaultComponent` prop to change the default avatar when ENS avatar is not found.
Use `loadingComponent` prop to change the loading placeholder: ```tsx twoslash import {
  Avatar
} from '@coinbase/onchainkit/identity';
<Avatar
  address="0x1234567890abcdef1234567890abcdef12345678"
  loadingComponent={
    // [!code focus]
    <div className="h-8 w-8">
      {" "}
      // [!code focus]
      <svg
        width="100%"
        height="100%"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        {" "}
        // [!code focus]
        <polygon
          points="6,1 14,1 19,6 19,14 14,19 6,19 1,14 1,6"
          fill="yellow"
          stroke="yellow"
          stroke-width="1"
        />{" "}
        // [!code focus]
      </svg>{" "}
      // [!code focus]
    </div> // [!code focus]
  } // [!code focus]
  defaultComponent={
    // [!code focus]
    <div className="h-8 w-8">
      {" "}
      // [!code focus]
      <svg
        width="100%"
        height="100%"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        {" "}
        // [!code focus]
        <polygon
          points="6,1 14,1 19,6 19,14 14,19 6,19 1,14 1,6"
          fill="green"
          stroke="green"
          stroke-width="1"
        />{" "}
        // [!code focus]
      </svg>{" "}
      // [!code focus]
    </div> // [!code focus]
  } // [!code focus]
/>
```
<App>
  <Avatar
    address="0x1234567890abcdef1234567890abcdef12345678"
    loadingComponent={
      <div className="h-8 w-8">
        <svg
          width="100%"
          height="100%"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <polygon
            points="6,1 14,1 19,6 19,14 14,19 6,19 1,14 1,6"
            fill="yellow"
            stroke="yellow"
            stroke-width="1"
          />
        </svg>
      </div>
    }
    defaultComponent={
      <div className="h-8 w-8">
        <svg
          width="100%"
          height="100%"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <polygon
            points="6,1 14,1 19,6 19,14 14,19 6,19 1,14 1,6"
            fill="green"
            stroke="green"
            stroke-width="1"
          />
        </svg>
      </div>
    }
  />
</App>
Show attestation on ENV avatar with [`Badge`](/identity/badge) component. Use [`OnchainKitProvider`](/config/onchainkit-provider)
or [`Identity`](/identity/identity) component with the `schemaId` prop. ```tsx twoslash
import {(Avatar, Badge, Identity)} from '@coinbase/onchainkit/identity'; // [!code
focus]
<Identity
  schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9" // [!code focus]
  address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
>
  <Avatar>
    {" "}
    // [!code focus]
    <Badge /> // [!code focus]
  </Avatar>{" "}
  // [!code focus]
</Identity>
```
<App>
  <Identity
    schemaId="0xf8b05c79f090979bf4a80270aba232dff11a10d9ca55c4f88de95317970f0de9"
    address="0x838aD0EAE54F99F1926dA7C3b6bFbF617389B4D9"
    className="bg-transparent"
  >
    <Avatar>
      <Badge />
    </Avatar>
  </Identity>
</App>
## Props [`AvatarReact`](/identity/types#AvatarReact)

der.mdx -->

# `<OnchainKitProvider />`

Provides the OnchainKit React Context to the app.

## Usage

```tsx twoslash
// @noErrors: 2304 - Cannot find name 'MyComponent'
import { base } from "viem/chains";
import { OnchainKitProvider } from "@coinbase/onchainkit";

const App = () => {
  return (
    <OnchainKitProvider
      config={{
        appearance: {
          name: "OnchainKit Playground",
          logo: "https://onchainkit.xyz/favicon/48x48.png?v4-19-24",
          mode: "auto",
          theme: "default",
        },
      }}
      chain={base}
    >
      <MyComponent />
    </OnchainKitProvider>
  );
};
```

## Props

[`OnchainKitProviderReact`](/config/types#onchainkitproviderreact)

--

title: OnchainKit top-level types
description: Glossary of OnchainKit top-level Types.

---

# Types [Glossary of general Types.]

## `AppConfig`

```ts
type AppConfig = {
  appearance?: {
    name?: string | null; // The name of your application
    logo?: string | null; // The URL of your application logo
    mode?: Mode | null; // Optionally determines color scheme based on OS preference or user selection
    theme?: ComponentTheme | null; // Optionally sets the visual style for components
  };
  paymaster?: string | null; // Paymaster URL for gas sponsorship
};
```

## `isBaseOptions`

```ts
type isBaseOptions = {
  chainId: number;
  isMainnetOnly?: boolean; // If the chainId check is only allowed on mainnet
};
```

## `isEthereumOptions`

```ts
type isEthereumOptions = {
  chainId: number;
  isMainnetOnly?: boolean; // If the chainId check is only allowed on mainnet
};
```

## `OnchainKitConfig`

```ts
type OnchainKitConfig = {
  address: Address | null; // Address is optional as we may not have an address for new users
  apiKey: string | null; // ApiKey for Coinbase Developer Platform APIs
  chain: Chain; // Chain must be provided as we need to know which chain to use
  config?: AppConfig; // Configuration options for the app
  rpcUrl: string | null; // RPC URL for onchain requests. Defaults to using CDP Node if the API Key is set
  schemaId: EASSchemaUid | null; // SchemaId is optional as not all apps need to use EAS
  projectId: string | null; // ProjectId from Coinbase Developer Platform, only required for Coinbase Onramp support
};
```

## `OnchainKitContextType`

```ts
type OnchainKitContextType = OnchainKitConfig;
```

## `OnchainKitProviderReact`

```ts
type OnchainKitProviderReact = {
  address?: Address;
  apiKey?: string;
  chain: Chain;
  children: ReactNode;
  config?: AppConfig;
  rpcUrl?: string;
  schemaId?: EASSchemaUid;
  projectId?: string;
};
```

-->

# `isEthereum`

The `isEthereum` utility is designed to verify if the chain id is a valid Ethereum Mainnet or Ethereum Sepolia chain id.

## Usage

:::code-group

```tsx twoslash [code]
import { isEthereum } from "@coinbase/onchainkit";

const chainId = 1;

if (isEthereum({ chainId })) {
  console.log("The chainId is Ethereum Mainnet or Ethereum Sepolia.");
} else {
  console.log("The chainId is not Ethereum.");
}
```

```ts [return value]
true;
```

:::

## Returns

`boolean` - Returns `true` if the chain id is Ethereum Mainnet or Ethereum Sepolia, otherwise `false`.

## Parameters

[`isEthereumOptions`](/config/types#isethereumoptions)

# `isBase`

The `isBase` utility is designed to verify if the chain id is a valid Base or Base Sepolia chain id.

## Usage

:::code-group

```tsx twoslash [code]
import { isBase } from "@coinbase/onchainkit";

const chainId = 8453;

if (isBase({ chainId })) {
  console.log("The chainId is Base.");
} else {
  console.log("The chainId is not Base.");
}
```

```ts [return value]
true;
```

:::

## Returns

`boolean` - Returns `true` if the chain id is Base or Base Sepolia, otherwise `false`.

## Parameters

[`isBaseOptions`](/config/types#isbaseoptions)

le: OnchainKit
description: React components and TypeScript utilities for onchain apps.
content:
width: 100%
layout: landing
showOutline: false

---

import { base } from "viem/chains";
import { OnchainKitProvider } from "@coinbase/onchainkit";
import {
Address,
Avatar,
Badge,
EthBalance,
Name,
Identity,
} from "@coinbase/onchainkit/identity";
import {
Swap,
SwapAmountInput,
SwapButton,
SwapMessage,
SwapToggleButton,
} from "@coinbase/onchainkit/swap";
import { color } from "@coinbase/onchainkit/theme";
import {
ConnectWallet,
Wallet,
WalletDropdown,
WalletDropdownBasename,
WalletDropdownLink,
WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import App from "../components/App";
import NavigationList from "../components/landing/NavigationList";
import SwapWrapper from "../components/SwapWrapper";
import TokenSelector from "../components/TokenSelector";
import WalletComponents from "../components/WalletComponents";
import TransactionWrapper from "../components/TransactionWrapper";
import FundWrapper from "../components/FundWrapper";
import {
Transaction,
TransactionButton,
TransactionSponsor,
TransactionStatus,
TransactionStatusAction,
TransactionStatusLabel,
} from "@coinbase/onchainkit/transaction";
import { FundButton } from "@coinbase/onchainkit/fund";
import Tweets from "../components/landing/Tweets";
import ComponentPreview from "../components/landing/ComponentPreview";
import LandingFooter from "../components/landing/LandingFooter";

<div className="max-w-[1225px] mx-auto vp-doc relative px-[24px] mb-[26px] mt-0 md:px-0 md:mb-[64px] pb-24">
  <div className="mx-auto max-w-2xl">
    <div className="md:text-center flex flex-col gap-6 pt-[100px] pb-8">
      <h1 className="text-center text-5xl md:text-7xl font-medium no-underline text-zinc-950 dark:text-zinc-50 tracking-[-0.1rem]">OnchainKit</h1>
      <div className="landing-page-hero text-center text-xl md:text-2xl text-zinc-950 dark:text-zinc-50">
          Build onchain apps with ready-to-use React components and Typescript utilities.
      </div>
    </div>
    <div className="flex flex-col items-center gap-6 w-full">
      <div id="home-install" className="h-full w-10/12">

:::code-group

```bash [npm]
npm install @coinbase/onchainkit
```

```bash [yarn]
yarn add @coinbase/onchainkit
```

```bash [pnpm]
pnpm add @coinbase/onchainkit
```

```bash [bun]
bun add @coinbase/onchainkit
```

:::

</div>
<a href="/getting-started" title="Get started with OnchainKit" className="alternate-button mx-auto md:mx-0 flex justify-center items-center bg-indigo-600 hover:bg-indigo-700 text-gray-50 dark:bg-indigo-400 dark:text-gray-950 dark:hover:bg-indigo-300 font-semibold leading-6 px-3 py-2 rounded-lg w-[140px]">
Get started
</a>
</div>

  </div>
</div>

<main className="items-center flex flex-col vp-doc relative">
  <div className="live-demo-section pt-12">
    <ComponentPreview />
  </div>
  <div className="testimonials-section pt-12">
    <Tweets />
  </div>
  <div className="footer-section pt-12">
    <LandingFooter />
  </div>
</main>

-->

---

title: <SwapSettings /> · OnchainKit
description: Customizable components for token Swap settings and slippage configuration

---

import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
Swap,
SwapAmountInput,
SwapButton,
SwapMessage,
SwapSettings,
SwapSettingsSlippageDescription,
SwapSettingsSlippageInput,
SwapSettingsSlippageTitle,
SwapToggleButton,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import SwapWrapper from "../../components/SwapWrapper";
import { walletDropdownLinkCustomBaseIconSvg } from "../../components/svg/walletDropdownLinkCustomBaseIconSvg";

# `SwapSettings`

The `SwapSettings` component enables customizable slippage configuration in the `Swap` component.

## Usage

```tsx twoslash
// omitted for brevity
import {
  Swap,
  SwapSettings, // [!code focus]
  SwapSettingsSlippageDescription, // [!code focus]
  SwapSettingsSlippageInput, // [!code focus]
  SwapSettingsSlippageTitle, // [!code focus]
} from "@coinbase/onchainkit/swap";

<Swap>
  <SwapSettings>
    // [!code focus]
    <SwapSettingsSlippageTitle>
      // [!code focus] Max. slippage// [!code focus]
    </SwapSettingsSlippageTitle>// [!code focus]
    <SwapSettingsSlippageDescription>
      // [!code focus] Your swap will revert if the prices change by more than
      the selected// [!code focus] percentage.// [!code focus]
    </SwapSettingsSlippageDescription>
    // [!code focus]
    <SwapSettingsSlippageInput />
    // [!code focus]
  </SwapSettings>
  // [!code focus]
</Swap>;
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapSettings>
              <SwapSettingsSlippageTitle>
                Max. slippage
              </SwapSettingsSlippageTitle>
              <SwapSettingsSlippageDescription>
                Your swap will revert if the prices change by more than the
                selected percentage.
              </SwapSettingsSlippageDescription>
              <SwapSettingsSlippageInput />
            </SwapSettings>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Override styles

You can override component styles using `className`.

```tsx twoslash
import {
  Swap,
  SwapSettings,
  SwapSettingsSlippageDescription,
  SwapSettingsSlippageInput,
  SwapSettingsSlippageTitle,
} from "@coinbase/onchainkit/swap";
// ---cut-before---
// omitted for brevity
<Swap>
  <SwapSettings>
    <SwapSettingsSlippageTitle className="text-[#EA580C]">
      // [!code focus] Max. slippage
    </SwapSettingsSlippageTitle>
    <SwapSettingsSlippageDescription className="text-[#EA580C]">
      // [!code focus] Your swap will revert if the prices change by more than
      the selected percentage.
    </SwapSettingsSlippageDescription>
    <SwapSettingsSlippageInput />
  </SwapSettings>
</Swap>;
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapSettings>
              <SwapSettingsSlippageTitle className="text-[#EA580C]">
                Max. slippage
              </SwapSettingsSlippageTitle>
              <SwapSettingsSlippageDescription className="text-[#EA580C]">
                Your swap will revert if the prices change by more than the
                selected percentage.
              </SwapSettingsSlippageDescription>
              <SwapSettingsSlippageInput />
            </SwapSettings>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Override icon

You can override the icon using the icon prop.

```tsx twoslash
// suppress twoslash error
declare const baseIcon: any;

import {
  Swap,
  SwapSettings,
  SwapSettingsSlippageDescription,
  SwapSettingsSlippageInput,
  SwapSettingsSlippageTitle,
} from "@coinbase/onchainkit/swap";
// ---cut-before---
// omitted for brevity
<SwapSettings icon={baseIcon}>
  // [!code focus] // ---cut-after---
</SwapSettings>;
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapSettings icon={walletDropdownLinkCustomBaseIconSvg}>
              <SwapSettingsSlippageTitle>
                Max. slippage
              </SwapSettingsSlippageTitle>
              <SwapSettingsSlippageDescription>
                Your swap will revert if the prices change by more than the
                selected percentage.
              </SwapSettingsSlippageDescription>
              <SwapSettingsSlippageInput />
            </SwapSettings>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Add text

You can add text next to the `SwapSettings` component using text.

```tsx twoslash
import {
  Swap,
  SwapSettings,
  SwapSettingsSlippageDescription,
  SwapSettingsSlippageInput,
  SwapSettingsSlippageTitle,
} from "@coinbase/onchainkit/swap";
// ---cut-before---
// omitted for brevity
<SwapSettings text="Settings">
  // [!code focus] // ---cut-after---
</SwapSettings>;
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapSettings text="Settings">
              <SwapSettingsSlippageTitle>
                Max. slippage
              </SwapSettingsSlippageTitle>
              <SwapSettingsSlippageDescription>
                Your swap will revert if the prices change by more than the
                selected percentage.
              </SwapSettingsSlippageDescription>
              <SwapSettingsSlippageInput />
            </SwapSettings>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Override text

You can override component text by providing children text.

```tsx twoslash
import {
  Swap,
  SwapSettings,
  SwapSettingsSlippageDescription,
  SwapSettingsSlippageInput,
  SwapSettingsSlippageTitle,
} from "@coinbase/onchainkit/swap";
<Swap>
  // ---cut-before--- // omitted for brevity
  <SwapSettingsSlippageTitle>
    Slippage Settings// [!code focus]
  </SwapSettingsSlippageTitle>
  <SwapSettingsSlippageDescription>
    Set a max slippage you are willing to accept.// [!code focus]
  </SwapSettingsSlippageDescription>
  // ---cut-after---
</Swap>;
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapSettings>
              <SwapSettingsSlippageTitle>
                Slippage Settings
              </SwapSettingsSlippageTitle>
              <SwapSettingsSlippageDescription>
                Set a max slippage you are willing to accept.
              </SwapSettingsSlippageDescription>
              <SwapSettingsSlippageInput />
            </SwapSettings>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

## Components

- `<SwapSettings />` - Container component for swap slippage settings.
- `<SwapSettingsSlippageDescription />` - Displays description text explaining the slippage setting.
- `<SwapSettingsSlippageInput />` - Input field for users to enter their desired max slippage percentage
- `<SwapSettingsSlippageTitle />` - Displays the title for the slippage settings section

## Props

- [`SwapsSettingsReact`](/swap/types#swapsettingsreact)
- [`SwapSettingsSlippageDescriptionReact`](/swap/types#swapsettingsslippagedescriptionreact)
- [`SwapSettingsSlippageInputReact`](/swap/types#swapsettingsslippageinputreact)
- [`SwapSettingsSlippageTitleReact`](/swap/types#swapsettingsslippagetitlereact)

title: Swap components & utilities Types
description: Glossary of Types in Swap components & utilities.

---

# Types [Glossary of Types in Swap components & utilities.]

## `Fee`

```ts
type Fee = {
  amount: string; // The amount of the fee
  baseAsset: Token; // The base asset for the fee
  percentage: string; // The percentage of the fee
};
```

## `QuoteWarning`

```ts
type QuoteWarning = {
  description?: string; // The description of the warning
  message?: string; // The message of the warning
  type?: string; // The type of the warning
};
```

## `LifecycleStatus`

```ts
type LifecycleStatusDataShared = {
  isMissingRequiredField: boolean;
  maxSlippage: number;
};

type LifecycleStatus =
  | {
      statusName: "init";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "error";
      statusData: SwapError & LifecycleStatusDataShared;
    }
  | {
      statusName: "amountChange";
      statusData: {
        amountFrom: string;
        amountTo: string;
        tokenFrom?: Token;
        tokenTo?: Token;
      } & LifecycleStatusDataShared;
    }
  | {
      statusName: "slippageChange";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "transactionPending";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "transactionApproved";
      statusData: {
        transactionHash: Hex;
        transactionType: "ERC20" | "Permit2";
      } & LifecycleStatusDataShared;
    }
  | {
      statusName: "success";
      statusData: {
        transactionReceipt: TransactionReceipt;
      } & LifecycleStatusDataShared;
    };
```

## `SwapAmountInputReact`

```ts
type SwapAmountInputReact = {
  className?: string; // Optional className override for top div element.
  delayMs?: number; // The debounce delay in milliseconds
  label: string; // Descriptive label for the input field
  swappableTokens?: Token[]; // Swappable tokens
  token?: Token; // Selected token
  type: "to" | "from"; // Identifies if component is for toToken or fromToken
};
```

## `SwapButtonReact`

```ts
type SwapButtonReact = {
  className?: string; // Optional className override for top div element.
  disabled?: boolean; // Disables swap button
};
```

## `SwapError`

```ts
type SwapError = {
  code: string; // The error code representing the type of swap error.
  error: string; // The error message providing details about the swap error.
  message: string; // The error message providing details about the swap error.
};
```

# `SwapMessageReact`

```ts
type SwapMessageReact = {
  className?: string; // Optional className override for top div element.
};
```

## `SwapQuote`

```ts
type SwapQuote = {
  amountReference: string; // The reference amount for the quote
  from: Token; // The source token for the swap
  fromAmount: string; // The amount of the source token
  fromAmountUSD: string; // The USD value of the source token
  hasHighPriceImpact: boolean; // Whether the price impact is high
  priceImpact: string; // The price impact of the swap
  slippage: string; // The slippage of the swap
  to: Token; // The destination token for the swap
  toAmount: string; // The amount of the destination token
  toAmountUSD: string; // The USD value of the destination token
  warning?: QuoteWarning; // The warning associated with the quote
};
```

## `SwapReact`

```ts
type SwapReact = {
  children: ReactNode;
  className?: string; // Optional className override for top div element.
  config?: SwapConfig;
  experimental?: {
    useAggregator: boolean; // Whether to use a DEX aggregator. (default: true)
  };
  isSponsored?: boolean; // An optional setting to sponsor swaps with a Paymaster. (default: false)
  onError?: (error: SwapError) => void; // An optional callback function that handles errors within the provider.
  onStatus?: (lifecycleStatus: LifecycleStatus) => void; // An optional callback function that exposes the component lifecycle state
  onSuccess?: (transactionReceipt: TransactionReceipt) => void; // An optional callback function that exposes the transaction receipt
  title?: string; // Title for the Swap component. (default: "Swap")
};
```

## `SwapDefaultReact`

```ts
export type SwapDefaultReact = {
  to: Token[]; // Swappable tokens (first token in array will be initial token selected)
  from: Token[]; // Swappable tokens (first token in array will be initial token selected)
  disabled?: boolean; // Disables swap button
} & Omit<SwapReact, "children">;
```

## `SwapSettingsReact`

```ts
type SwapSettingsReact = {
  children: ReactNode;
  className?: string; // Optional className override for top div element.
  icon?: ReactNode; // Optional icon override
  text?: string; // Optional text override
};
```

## `SwapSettingsSlippageDescriptionReact`

```ts
type SwapSettingsSlippageDescriptionReact = {
  children: ReactNode;
  className?: string; // Optional className override for top div element.
};
```

## `SwapSettingsSlippageInputReact`

```ts
type SwapSettingsSlippageInputReact = {
  className?: string; // Optional className override for top div element.
};
```

## `SwapSettingsSlippageTitleReact`

```ts
type SwapSettingsSlippageTitleReact = {
  children: ReactNode;
  className?: string; // Optional className override for top div element.
};
```

## `SwapToastReact`

```ts
type SwapToastReact = {
  className?: string; // An optional CSS class name for styling the toast component.
  durationMs?: number; // An optional value to customize time until toast disappears
  position?: "top-center" | "top-right" | "bottom-center" | "bottom-right"; // An optional position property to specify the toast's position on the screen.
};
```

## `SwapToggleButtonReact`

```ts
type SwapToggleButtonReact = {
  className?: string; // Optional className override for top div element.
};
```

## `Transaction`

```ts
type Transaction = {
  chainId: number; // The chain ID
  data: Hex; // The data for the transaction
  gas: bigint; // The gas limit
  maxFeePerGas?: bigint | undefined; // The maximum fee per gas
  maxPriorityFeePerGas?: bigint | undefined; // The maximum priority fee per gas
  nonce?: number; // The nonce for the transaction
  to: Address; // The recipient address
  value: bigint; // The value of the transaction
};
```

title: <Swap /> · OnchainKit
description: Swap components & utilities

---

import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
Swap,
SwapAmountInput,
SwapButton,
SwapDefault,
SwapMessage,
SwapToggleButton,
SwapToast,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import SwapWrapper from "../../components/SwapWrapper";

# `<Swap />`

The `Swap` components provide a comprehensive interface for users to execute [Token](/token/types#token) swaps.

Before using them, ensure you've completed all [Getting Started steps](/getting-started).

## Quick start

The `SwapDefault` component is a simplified version of the `Swap` component, designed to streamline the integration process for developers. Instead of manually defining each subcomponent and prop, developers can use this shorthand version which renders our suggested implementation of the component and includes `SwapAmountInput`, `SwapSettings`, `SwapToggleButton`, `SwapButton`, and `SwapToast`.

If you'd like more customization, follow the implementation guide for our `Swap` component below.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import { SwapDefault } from "@coinbase/onchainkit/swap"; // [!code focus]
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const degenToken: Token = {
    name: "DEGEN",
    address: "0x4ed4e862860bed51a9570b96d89af5e1b0efefed",
    symbol: "DEGEN",
    decimals: 18,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/3b/bf/3bbf118b5e6dc2f9e7fc607a6e7526647b4ba8f0bea87125f971446d57b296d2-MDNmNjY0MmEtNGFiZi00N2I0LWIwMTItMDUyMzg2ZDZhMWNm",
    chainId: 8453,
  };

  const ethToken: Token = {
    name: "ETH",
    address: "",
    symbol: "ETH",
    decimals: 18,
    image:
      "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
    chainId: 8453,
  };

  const usdcToken: Token = {
    name: "USDC",
    address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
    symbol: "USDC",
    decimals: 6,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
    chainId: 8453,
  };

  const wethToken: Token = {
    name: "Wrapped Ether",
    address: "0x4200000000000000000000000000000000000006",
    symbol: "WETH",
    decimals: 6,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/47/bc/47bc3593c2dec7c846b66b7ba5f6fa6bd69ec34f8ebb931f2a43072e5aaac7a8-YmUwNmRjZDUtMjczYy00NDFiLWJhZDUtMzgwNjFmYWM0Njkx",
    chainId: 8453,
  };
  // ---cut-before---
  // omitted for brevity

  // the first token in array will be initially selected token // [!code focus]
  const swappableFromTokens: Token[] = [
    wethToken,
    usdcToken,
    ethToken,
    degenToken,
  ]; // [!code focus]
  const swappableToTokens: Token[] = [
    degenToken,
    ethToken,
    usdcToken,
    wethToken,
  ]; // [!code focus]

  return (
    // [!code focus]
    <SwapDefault // [!code focus]
      from={swappableFromTokens} // [!code focus]
      to={swappableToTokens} // [!code focus]
    /> // [!code focus]
  ); // [!code focus]
  // ---cut-after---
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <SwapDefault
            from={swappableTokens}
            to={swappableTokens.slice().reverse()}
          />
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Props

[`SwapDefaultReact`](/swap/types#swapdefaultreact)

## Usage

Example using `@coinbase/onchainkit/swap` and `@coinbase/onchainkit/wallet`.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  // [!code focus]
  Swap, // [!code focus]
  SwapAmountInput, // [!code focus]
  SwapToggleButton, // [!code focus]
  SwapButton, // [!code focus]
  SwapMessage, // [!code focus]
  SwapToast, // [!code focus]
} from "@coinbase/onchainkit/swap"; // [!code focus]
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  // add other tokens here to display them as options in the swap
  const swappableTokens: Token[] = [ETHToken, USDCToken];

  return address ? (
    <Swap>
      {" "}
      // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Sell" // [!code focus]
        swappableTokens={swappableTokens} // [!code focus]
        token={ETHToken} // [!code focus]
        type="from" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapToggleButton /> // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Buy" // [!code focus]
        swappableTokens={swappableTokens} // [!code focus]
        token={USDCToken} // [!code focus]
        type="to" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapButton /> // [!code focus]
      <SwapMessage /> // [!code focus]
      <SwapToast /> // [!code focus]
    </Swap> // [!code focus]
  ) : (
    <Wallet>
      <ConnectWallet>
        <Avatar className="h-6 w-6" />
        <Name />
      </ConnectWallet>
    </Wallet>
  );
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton disabled />
            <SwapMessage />
            <SwapToast />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

:::danger
**Note: This interface is for demonstration purposes only.**

The swap will execute and work out of the box when you implement the component in your own app.
:::

### Sponsor gas with Paymaster

To sponsor swap transactions for your users, toggle the Paymaster using the `isSponsored` prop.

By default, this will use the [Coinbase Developer Platform](https://portal.cdp.coinbase.com/products/bundler-and-paymaster) Paymaster.

You can configure sponsorship settings on the [Paymaster](https://portal.cdp.coinbase.com/products/bundler-and-paymaster) page.
For security reasons, we recommend setting up a contract allowlist in the Portal. Without a contract allowlist defined, your Paymaster will only be able to sponsor up to $1.

The contract used in our Swap API is Uniswap's [Universal Router](https://basescan.org/address/0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD), which is deployed on Base at `0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD`.

Note that gas sponsorship will only work for Smart Wallets.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  Swap,
  SwapAmountInput,
  SwapToggleButton,
  SwapButton,
  SwapMessage,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  return (
    // ---cut-before---
    // omitted for brevity

    // Set isSponsored to true // [!code focus]
    <Swap isSponsored> // [!code focus] ...</Swap> // [!code focus]
    // ---cut-after---
  );
}
```

### Custom token pair

You can adjust to only allow swap between a token pair.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  Swap,
  SwapAmountInput,
  SwapToggleButton,
  SwapButton,
  SwapMessage,
  SwapToast,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  return (
    // ---cut-before---
    // omitted for brevity

    <Swap>
      {" "}
      // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Sell" // [!code focus]
        token={ETHToken} // [!code focus]
        type="from" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapToggleButton /> // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Buy" // [!code focus]
        token={USDCToken} // [!code focus]
        type="to" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapButton /> // [!code focus]
      <SwapMessage /> // [!code focus]
      <SwapToast /> // [!code focus]
    </Swap> // [!code focus]
    // ---cut-after---
  );
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapAmountInput
              label="Sell"
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput label="Buy" token={swappableTokens[2]} type="to" />
            <SwapButton disabled />
            <SwapMessage />
            <SwapToast />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Remove toggle button

You can remove `SwapToggleButton` to make swap unidirectional.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  Swap,
  SwapAmountInput,
  SwapToggleButton,
  SwapButton,
  SwapMessage,
  SwapToast,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  return (
    // ---cut-before---
    // omitted for brevity

    <Swap>
      {" "}
      // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Sell" // [!code focus]
        token={ETHToken} // [!code focus]
        type="from" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Buy" // [!code focus]
        token={USDCToken} // [!code focus]
        type="to" // [!code focus]
      /> // [!code focus]
      <SwapButton /> // [!code focus]
      <SwapMessage /> // [!code focus]
      <SwapToast /> // [!code focus]
    </Swap> // [!code focus]
    // ---cut-after---
  );
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapAmountInput
              label="Sell"
              token={swappableTokens[1]}
              type="from"
            />
            <SwapAmountInput label="Buy" token={swappableTokens[2]} type="to" />
            <SwapButton disabled />
            <SwapMessage />
            <SwapToast />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Remove swap message

You can remove `SwapMessage` component.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  Swap,
  SwapAmountInput,
  SwapToggleButton,
  SwapButton,
  SwapMessage,
  SwapToast,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  return (
    // ---cut-before---
    // omitted for brevity

    <Swap>
      {" "}
      // [!code focus]
      <SwapAmountInput // [!code focus]
        label="Sell" // [!code focus]
        token={ETHToken} // [!code focus]
        type="from" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapToggleButton />
      <SwapAmountInput // [!code focus]
        label="Buy" // [!code focus]
        token={USDCToken} // [!code focus]
        type="to" // [!code focus]
      />{" "}
      // [!code focus]
      <SwapButton /> // [!code focus]
      <SwapToast /> // [!code focus]
    </Swap> // [!code focus]
    // ---cut-after---
  );
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapAmountInput
              label="Sell"
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton />
            <SwapAmountInput label="Buy" token={swappableTokens[2]} type="to" />
            <SwapButton disabled />
            <SwapToast />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

### Override styles

You can override component styles using `className`.

```tsx twoslash
import { Avatar, Name } from "@coinbase/onchainkit/identity";
import {
  Swap,
  SwapAmountInput,
  SwapToggleButton,
  SwapButton,
  SwapMessage,
  SwapToast,
} from "@coinbase/onchainkit/swap";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import { useAccount } from "wagmi";
import type { Token } from "@coinbase/onchainkit/token";

export default function SwapComponents() {
  const { address } = useAccount();

  const ETHToken: Token = {
    address: "",
    chainId: 8453,
    decimals: 18,
    name: "Ethereum",
    symbol: "ETH",
    image:
      "https://dynamic-assets.coinbase.com/dbb4b4983bde81309ddab83eb598358eb44375b930b94687ebe38bc22e52c3b2125258ffb8477a5ef22e33d6bd72e32a506c391caa13af64c00e46613c3e5806/asset_icons/4113b082d21cc5fab17fc8f2d19fb996165bcce635e6900f7fc2d57c4ef33ae9.png",
  };

  const USDCToken: Token = {
    address: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    chainId: 8453,
    decimals: 6,
    name: "USDC",
    symbol: "USDC",
    image:
      "https://dynamic-assets.coinbase.com/3c15df5e2ac7d4abbe9499ed9335041f00c620f28e8de2f93474a9f432058742cdf4674bd43f309e69778a26969372310135be97eb183d91c492154176d455b8/asset_icons/9d67b728b6c8f457717154b3a35f9ddc702eae7e76c4684ee39302c4d7fd0bb8.png",
  };

  return (
    // ---cut-before---
    // omitted for brevity

    <Swap>
      <SwapAmountInput label="Sell" token={ETHToken} type="from" />
      <SwapToggleButton className="border-[#EA580C]" /> // [!code focus]
      <SwapAmountInput label="Buy" token={USDCToken} type="to" />
      <SwapButton className="bg-[#EA580C]" /> // [!code focus]
      <SwapMessage />
      <SwapToast />
    </Swap>
    // ---cut-after---
  );
}
```

<App>
  <SwapWrapper>
    {({ address, swappableTokens }) => {
      if (address) {
        return (
          <Swap>
            <SwapAmountInput
              label="Sell"
              swappableTokens={swappableTokens}
              token={swappableTokens[1]}
              type="from"
            />
            <SwapToggleButton className="border-[#EA580C]" />
            <SwapAmountInput
              label="Buy"
              swappableTokens={swappableTokens}
              token={swappableTokens[2]}
              type="to"
            />
            <SwapButton className="bg-[#EA580C]" disabled />
            <SwapMessage />
            <SwapToast />
          </Swap>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </SwapWrapper>
</App>

## Components

The components are designed to work together hierarchically. For each component, ensure the following:

- `<Swap />` - Set the user's address and error handling.
- `<SwapAmountInput />` - Set the [Token](/token/types#token) to swap and specify the input type (`from` or `to`).
- `<SwapToggleButton />` - Optional component to toggle between input types.
- `<SwapMessage />` - Optional component that displays a message related to the swap operation's current state.
- `<SwapButton />` - Set the onSuccess and onError callbacks.
- `<SwapToast />` - Optional component to notify user of successful swap transaction.

## Props

- [`SwapReact`](/swap/types#swapreact)
- [`SwapDefaultReact`](/swap/types#swapdefaultreact)
- [`SwapAmountInputReact`](/swap/types#swapamountinputreact)
- [`SwapButtonReact`](/swap/types#swapbuttonreact)
- [`SwapMessageReact`](/swap/types#swapmessagereact)
- [`SwapToggleButtonReact`](/swap/types#swaptogglebuttonreact)
- [`SwapToastReact`](/swap/types#swaptoastreactt)

x -->

---

title: <FrameMetadata /> · OnchainKit
description: FrameMetadata components & utilities

---

# `<FrameMetadata />`

This component is utilized for incorporating Frame metadata elements into the React page.

Note: If you are using Next.js with App routing, it is recommended to use `getFrameMetadata` instead.

## Usage

:::code-group

```tsx twoslash [code]
// @noErrors
import { FrameMetadata } from '@coinbase/onchainkit/frame';

export default function HomePage() {
  return (
    ...
    <FrameMetadata
      buttons={[
        {
          label: 'Tell me the story',
        },
        {
          action: 'link',
          label: 'Link to Google',
          target: 'https://www.google.com'
        },
        {
          action: 'post_redirect',
          label: 'Redirect to cute pictures',
        },
      ]}
      image={{
       src: 'https://zizzamia.xyz/park-3.png',
       aspectRatio: '1:1'
      }}
      input={{
        text: 'Tell me a boat story',
      }}
      state={{
        counter: 1,
      }}
      postUrl="https://zizzamia.xyz/api/frame"
    />
    ...
  );
}
```

```html [return html]
<meta name="fc:frame" content="vNext" />
<meta name="fc:frame:button:1" content="Tell me the story" />
<meta name="fc:frame:button:2" content="Link to Google" />
<meta name="fc:frame:button:2:action" content="link" />
<meta name="fc:frame:button:2:target" content="https://www.google.com" />
<meta name="fc:frame:button:3" content="Redirect to cute pictures" />
<meta name="fc:frame:button:3:action" content="post_redirect" />
<meta name="fc:frame:image" content="https://zizzamia.xyz/park-3.png" />
<meta name="fc:frame:image:aspect_ratio" content="1:1" />
<meta name="fc:frame:input:text" content="Tell me a boat story" />
<meta name="fc:frame:state" content="%7B%22counter%22%3A1%7D" />
<meta name="fc:frame:post_url" content="https://zizzamia.xyz/api/frame" />
```

:::

## Props

[`FrameMetadataReact`](/frame/types#framemetadatareact)

.mdx -->

# `getFrameMessage`

When a user interacts with your Frame, you receive a JSON message called
the "**Frame Signature Packet**". Decode and validate this message using the `getFrameMessage` function.

Note that if the `message` is not valid, it will be undefined.

## Usage

```ts twoslash
// @noErrors: 2307 1128 - Cannot find module 'next/server', Declaration or statement expected
import { FrameRequest, getFrameMessage } from '@coinbase/onchainkit/frame'; // [!code focus]
import { NextRequest, NextResponse } from 'next/server';

async function getResponse(req: NextRequest): Promise<NextResponse> {
  const frameRequest: FrameRequest = await req.json();
  const { isValid, message } = await getFrameMessage(frameRequest); // [!code focus]

  if (isValid) {
    // the message is valid
  }
  ...
}
```

## Returns

[`Promise<FrameValidationResponse>`](/frame/types#framevalidationresponse)

## Parameters

### FrameRequest

- [`FrameRequest`](/frame/types#framerequest)

### options.neynarApiKey

- **Type:** `string`

Default to OnchainKit's default key.

```ts twoslash
// @noErrors: 2307 - Cannot find module 'next/server'
import { FrameRequest, getFrameMessage } from "@coinbase/onchainkit/frame"; // [!code focus]
import { NextRequest, NextResponse } from "next/server";

async function getResponse(req: NextRequest): Promise<NextResponse> {
  const frameRequest: FrameRequest = await req.json();
  // ---cut-before---
  const { isValid, message } = await getFrameMessage(frameRequest, {
    neynarApiKey: "MY_NEYNAR_API_KEY", // [!code focus]
  });
  // ---cut-after---
}
```

### options.castReactionContext

- **Type:** `boolean`

Whether to cast the reaction context. Default: true

```ts twoslash
// @noErrors: 2307 - Cannot find module 'next/server'
import { FrameRequest, getFrameMessage } from "@coinbase/onchainkit/frame"; // [!code focus]
import { NextRequest, NextResponse } from "next/server";

async function getResponse(req: NextRequest): Promise<NextResponse> {
  const frameRequest: FrameRequest = await req.json();
  // ---cut-before---
  const { isValid, message } = await getFrameMessage(frameRequest, {
    castReactionContext: true, // [!code focus]
  });
  // ---cut-after---
}
```

### options.followContext

- **Type:** `boolean`

Whether to follow the context. Default: true

```ts twoslash
// @noErrors: 2307 - Cannot find module 'next/server'
import { FrameRequest, getFrameMessage } from "@coinbase/onchainkit/frame"; // [!code focus]
import { NextRequest, NextResponse } from "next/server";

async function getResponse(req: NextRequest): Promise<NextResponse> {
  const frameRequest: FrameRequest = await req.json();
  // ---cut-before---
  const { isValid, message } = await getFrameMessage(frameRequest, {
    followContext: true, // [!code focus]
  });
  // ---cut-after---
}
```

sponse.mdx -->

# `getFrameHtmlResponse`

When you need to send an HTML Frame Response, the `getFrameHtmlResponse` method is here to assist you.

It generates a valid HTML string response with a frame and utilizes `FrameMetadata` types for page metadata. This eliminates the need to manually create server-side HTML strings.

## Usage

```ts twoslash
// @noErrors: 2307 1128 - Cannot find module 'next/server', Declaration or statement expected
// Step 1. import getFrameHtmlResponse from @coinbase/onchainkit
import { getFrameHtmlResponse } from '@coinbase/onchainkit/frame';
import { NextRequest, NextResponse } from 'next/server';

async function getResponse(req: NextRequest): Promise<NextResponse> {
  // Step 2. Build your Frame logic
  ...

  return new NextResponse(
    // Step 3. Use getFrameHtmlResponse to create a Frame response
    getFrameHtmlResponse({
      buttons: [
        {
          label: `We love BOAT`,
        },
      ],
      image: 'https://build-onchain-apps.vercel.app/release/v-0-17.png',
      postUrl: 'https://build-onchain-apps.vercel.app/api/frame',
    }),
  );
}

export async function POST(req: NextRequest): Promise<Response> {
  return getResponse(req);
};
```

## Returns

```ts
type FrameHTMLResponse = string;
```

## Parameters

[`FrameMetadataType`](/frame/types#framemetadatatype)

-

title: Frame Types
description: Glossary of Types for Frame utilities and components

---

# Types [Glossary of Types for Frame utilities and components]

## `FrameButtonMetadata`

```ts
type FrameButtonMetadata =
  | {
      action: "link" | "mint";
      label: string;
      target: string;
    }
  | {
      action?: "post" | "post_redirect";
      label: string;
      target?: string;
    }
  | {
      action: "tx";
      label: string;
      target: string;
      postUrl?: string;
    };
```

## `FrameData`

```ts
interface FrameData {
  buttonIndex: number;
  castId: {
    fid: number;
    hash: string;
  };
  inputText: string;
  fid: number;
  messageHash: string;
  network: number;
  state: string;
  timestamp: number;
  transactionId?: string;
  url: string;
}
```

## `FrameImageMetadata`

```ts
type FrameImageMetadata = {
  src: string;
  aspectRatio?: "1.91:1" | "1:1";
};
```

## `FrameInputMetadata`

```ts
type FrameInputMetadata = {
  text: string;
};
```

## `FrameMetadataResponse`

```ts
type FrameMetadataResponse = Record<string, string>;
```

## `FrameMetadataReact`

```ts
type FrameMetadataReact = FrameMetadataType & {
  ogDescription?: string;
  ogTitle?: string;
  wrapper?: React.ComponentType<any>;
};
```

## `FrameMetadataType`

```ts
type FrameMetadataType = {
  accepts?: {
    [protocolIdentifier: string]: string;
  }; // The minimum client protocol version accepted for the given protocol identifier.
  buttons?: [FrameButtonMetadata, ...FrameButtonMetadata[]]; // A list of strings which are the label for the buttons in the frame (max 4 buttons).
  image: string | FrameImageMetadata; // An image which must be smaller than 10MB and should have an aspect ratio of 1.91:1
  input?: FrameInputMetadata; // The text input to use for the Frame.
  isOpenFrame?: boolean; // A boolean indicating if the frame uses the Open Frames standard.
  postUrl?: string; // A valid POST URL to send the Signature Packet to.
  refreshPeriod?: number; // A period in seconds at which the app should expect the image to update.
  state?: object; // A string containing serialized state (e.g. JSON) passed to the frame server.
};
```

## `FrameRequest`

```ts
interface FrameRequest {
  untrustedData: FrameData;
  trustedData: {
    messageBytes: string;
  };
}
```

## `FrameValidationData`

```ts
interface FrameValidationData {
  address: string | null; // The connected wallet address of the interacting user.
  button: number; // Number of the button clicked
  following: boolean; // Indicates if the viewer clicking the frame follows the cast author
  input: string; // Text input from the viewer typing in the frame
  interactor: {
    fid: number; // Viewer Farcaster ID
    custody_address: string; // Viewer custody address
    verified_accounts: string[]; // Viewer account addresses
    verified_addresses: {
      eth_addresses: string[] | null;
      sol_addresses: string[] | null;
    };
  };
  liked: boolean; // Indicates if the viewer clicking the frame liked the cast
  raw: NeynarFrameValidationInternalModel;
  recasted: boolean; // Indicates if the viewer clicking the frame recasted the cast
  state: {
    serialized: string; // Serialized state (e.g. JSON) passed to the frame server
  };
  transaction: {
    hash: string;
  } | null;
  valid: boolean; // Indicates if the frame is valid
}
```

## `FrameValidationResponse`

```ts
type FrameValidationResponse =
  | { isValid: true; message: FrameValidationData }
  | { isValid: false; message: undefined };
```

## `FrameTransactionResponse`

```ts
type ChainNamespace = "eip155" | "solana";
type ChainReference = string;

type FrameTransactionResponse = {
  chainId: `${ChainNamespace}:${ChainReference}`; // A CAIP-2 chain ID to identify the tx network
  method: "eth_sendTransaction"; // A method ID to identify the type of tx request.
  params: FrameTransactionEthSendParams; // Specific parameters for chainId and method
};
```

## `FrameTransactionEthSendParams`

```ts
type FrameTransactionEthSendParams = {
  abi: Abi; // The contract ABI for the contract to call.
  data?: Hex; // The data to send with the transaction.
  to: Address; // The address of the contract to call.
  value: bigint; // The amount of Ether to send with the transaction.
};
```

a.mdx -->

# `getFrameMetadata`

With Next.js App routing, use the `getFrameMetadata()` inside your `page.ts` to get the metadata need it for your Frame.

## Usage

```ts twoslash
// @noErrors: 2307 1005 1161 - Cannot find module 'next', Cannot find module './home'
// Step 1. import getFrameMetadata from @coinbase/onchainkit
import { getFrameMetadata } from "@coinbase/onchainkit/frame";
import type { Metadata } from "next";
import HomePage from "./home";

// Step 2. Use getFrameMetadata to shape your Frame metadata
const frameMetadata = getFrameMetadata({
  buttons: [
    {
      label: "We love BOAT",
    },
  ],
  image: "https://build-onchain-apps.vercel.app/release/v-0-17.png",
  postUrl: "https://build-onchain-apps.vercel.app/api/frame",
});

// Step 3. Add your metadata in the Next.js metadata utility
export const metadata: Metadata = {
  manifest: "/manifest.json",
  other: {
    ...frameMetadata,
  },
};

export default function Page() {
  return <HomePage />;
}
```

## Returns

[`FrameMetadataResponse`](/frame/types#framemetadataresponse)

## Parameters

[`FrameMetadataType`](/frame/types#framemetadatatype)

->

---

title: <Checkout /> · OnchainKit
description: One-click checkout for onchain commerce

---

import {
Checkout,
CheckoutButton,
CheckoutStatus,
} from "@coinbase/onchainkit/checkout";

# `<Checkout />`

The `Checkout` component provides a one-click checkout experience for onchain commerce.

Our all-in-one solution simplifies payment processing for onchain developers, removing complex integrations, high fees, and onboarding friction. Whether you're selling digital goods, services, or in-game items, this tool is for you.

<img
  alt="Checkout"
  src="https://onchainkit.xyz/assets/checkout.gif"
  height="364"
/>

## Features

- **Plug-and-Play Integration:** Add our `Checkout` button with just a few lines of code. No backend required.
- **Seamless Onboarding:** Support Passkey wallets to eliminate onboarding drop-offs.
- **Real-time Merchant Tooling:** Get instant payment tracking, analytics, and reporting.

## Prerequisites

Before using the `Checkout` component, ensure you've completed the [Getting Started](/getting-started) steps.

To use the `Checkout` component, you'll need to provide an API Key in `OnchainKitProvider`. You can get one following our [Getting Started](/getting-started#get-your-public-api-key) steps.

### Starting a new project

If you're starting a new project, we recommend using `create onchain` to scaffold your project.

```bash
npm create onchain@latest
```

### Adding to an existing project

If you're adding `Checkout` to an existing project, simply install OnchainKit.

:::code-group

```bash [npm]
npm install @coinbase/onchainkit
```

```bash [yarn]
yarn add @coinbase/onchainkit
```

```bash [pnpm]
pnpm add @coinbase/onchainkit
```

```bash [bun]
bun add @coinbase/onchainkit
```

:::

Wrap the `<OnchainKitProvider />` around your app, following the steps in [Getting Started](/getting-started#add-providers).

## Quickstart

::::steps

### Sign up for a Coinbase Commerce account

<img
  alt="Create a product"
  src="https://onchainkit.xyz/assets/commerce-1.png"
  height="364"
/>
Head to [Coinbase Commerce](https://beta.commerce.coinbase.com/) and sign up. This
is where you’ll manage transactions, view reports, and configure payments.

### Create a product and copy the `productId`

{" "}

<img
  alt="Copy productId"
  src="https://onchainkit.xyz/assets/commerce-2.png"
  height="364"
/>
In the Coinbase Commerce dashboard, create a new product and copy the `productId`.

### Import the component

```tsx twoslash
import {
  Checkout,
  CheckoutButton,
  CheckoutStatus,
} from "@coinbase/onchainkit/checkout";

<Checkout productId="my-product-id">
  <CheckoutButton coinbaseBranded /> // set coinbaseBranded for branding
  <CheckoutStatus />
</Checkout>;
```

::::

That's it! Starting selling onchain with just a few lines of code.

## Usage

### Configuring a checkout

You can create products on the Coinbase Commerce Portal and use them in the `Checkout` component through the `productId` prop.

If you'd like to create product metadata programmatically or implement a multi-product checkout, please see [Advanced Usage](/checkout/checkout#advanced-usage).

Coinbase Commerce charges a [1% fee](https://help.coinbase.com/en/commerce/getting-started/fees) associated with all payments.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

export default function PayComponents() {
  return (
    // ---cut-before---
    <Checkout productId="my-product-id">
      {" "}
      // [!code focus]
      <CheckoutButton />
    </Checkout>
    // ---cut-after---
  );
}
```

<App>
  <Checkout>
    <CheckoutButton disabled />
  </Checkout>
</App>

### Handling a successful checkout

To handle successful checkouts, use the `onStatus` prop to listen for the `success` callback.

This callback will return a [LifecycleStatusData](/checkout/checkout#advanced-usage) object including the [TransactionReceipt](https://github.com/wevm/viem/blob/main/src/types/transaction.ts#L38) and `chargeId`.

For idempotent actions, like rendering your own success screen, you can simply check that the `statusName` is equal to `success`.

For non-idempotent actions, like order fulfillment, we recommend one of the following approaches to verify a charge has been fully paid.

1. (**Recommended**) Check the status of the `chargeId` using the [Coinbase Commerce API](https://docs.cdp.coinbase.com/commerce-onchain/docs/web3-payments-faq#how-can-i-verify-if-a-charge-has-been-fully-paid).
2. Set up a [Coinbase Commerce Webhook](https://docs.cdp.coinbase.com/commerce-onchain/docs/webhooks) which will notify you for successful payments.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";
// ---cut-before---
import type { LifecycleStatus } from "@coinbase/onchainkit/checkout"; // [!code focus]

const statusHandler = async (status: LifecycleStatus) => {
  // [!code focus]
  const { statusName, statusData } = status; // [!code focus]
  switch (
    statusName // [!code focus]
  ) {
    case "success": // [!code focus]
      // handle success // [!code focus]
      const { chargeId } = statusData; // [!code focus]
      // use the charges api to verify the chargeId // [!code focus]
      const options = {
        // [!code focus]
        method: "GET", // [!code focus]
        headers: {
          // [!code focus]
          "Content-Type": "application/json", // [!code focus]
          Accept: "application/json", // [!code focus]
          "X-CC-Api-Key": "your_api_key_here", // Replace this with your Coinbase Commerce API Key // [!code focus]
        }, // [!code focus]
      }; // [!code focus]
      const response = await fetch(
        `https://api.commerce.coinbase.com/charges/${chargeId}`
      ); // [!code focus]
  } // [!code focus]
}; // [!code focus]

<Checkout onStatus={statusHandler}>
  {" "}
  // [!code focus]
  <CheckoutButton />
</Checkout>;
// ---cut-after---
```

:::tip[Coinbase Commerce API]
This is an authenticated endpoint. To verify charges, you'll need a Coinbase Commerce [API Key](https://docs.cdp.coinbase.com/commerce-onchain/docs/getting-started).
:::

:::danger[⚠️ Warning]
You should protect your Coinbase Commerce API Key by verifying charges server-side. This client-side code is only provided as an example.
:::

### Viewing successful checkouts

You can view successful checkouts on the [Coinbase Commerce Merchant Dashboard](https://beta.commerce.coinbase.com/payments).

<img
  alt="Viewing successful checkouts"
  src="https://onchainkit.xyz/assets/commerce-3.png"
  height="364"
/>

## Customization

### Add name and logo

To customize the name and logo of your application rendered in the popup, set the `name` and `logo` values inside [OnchainKitProvider](/config/onchainkit-provider#usage).

```tsx twoslash [providers.tsx]
// @noErrors: 2304 - Cannot find name 'children'
import { base } from "wagmi/chains";
// ---cut-before---
import { OnchainKitProvider } from "@coinbase/onchainkit";

<OnchainKitProvider
  chain={base}
  config={{
    appearance: {
      name: "OnchainKit Playground", // [!code ++]
      logo: "https://onchainkit.xyz/favicon/48x48.png?v4-19-24", // [!code ++]
    },
  }}
>
  {children}
</OnchainKitProvider>;
// ---cut-after---
```

<div style={{ display: "flex", justifyContent: "center" }}>
  <img
    alt="Add name and logo"
    src="https://onchainkit.xyz/assets/commerce-4.png"
  />
</div>

### Add Coinbase branding

You can add Coinbase branding to the component by using the `coinbaseBranded` prop on `CheckoutButton`.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

export default function PayComponents() {
  return (
    // ---cut-before---
    <Checkout>
      <CheckoutButton coinbaseBranded /> // [!code focus]
    </Checkout>
    // ---cut-after---
  );
}
```

<App>
  <Checkout>
    <CheckoutButton coinbaseBranded disabled />
  </Checkout>
</App>

### Disabling the button

You can disable the button using the `disabled` prop on `CheckoutButton`.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

export default function PayComponents() {
  return (
    // ---cut-before---
    <Checkout>
      <CheckoutButton disabled /> // [!code focus]
    </Checkout>
    // ---cut-after---
  );
}
```

<App>
  <Checkout>
    <CheckoutButton disabled />
  </Checkout>
</App>

### Customize button

You can customize the button text using the `text` prop on `CheckoutButton`.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

export default function PayComponents() {
  return (
    // ---cut-before---
    <Checkout>
      <CheckoutButton text="Checkout with USDC" /> // [!code focus]
    </Checkout>
    // ---cut-after---
  );
}
```

<App>
  <Checkout>
    <CheckoutButton text="Checkout with USDC" disabled />
  </Checkout>
</App>

### Override styles

We recommend style customization by setting a custom [OnchainKit theme](/guides/themes#custom-theme). You can also override individual component styles using `className`.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

export default function PayComponents() {
  return (
    // ---cut-before---
    <Checkout>
      <CheckoutButton className="bg-[#EA580C]" /> // [!code focus]
    </Checkout>
    // ---cut-after---
  );
}
```

<App>
  <Checkout>
    <CheckoutButton className="bg-[#EA580C]" disabled />
  </Checkout>
</App>

## Advanced Usage

### Shopping Carts and Multi-Product Checkout

You can accept payments for arbitrary product metadata using the Coinbase Commerce [create charge](https://docs.cdp.coinbase.com/commerce-onchain/reference/creates-a-charge) endpoint. This is useful if you have an existing inventory management system or want to implement custom features like multi-product checkouts, carts, etc.

:::tip[Coinbase Commerce API]
This is an authenticated endpoint. To create charges, you'll need a Coinbase Commerce [API Key](https://docs.cdp.coinbase.com/commerce-onchain/docs/getting-started).
:::

#### Example server side code

This Typescript example uses [Express](https://expressjs.com/) and [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

```tsx twoslash [server.ts]
import express, { Request, Response } from "express";
const fetch = require("node-fetch");

const app = express();
const port = 3000;

app.use(express.json());

// ---cut-before---
// This endpoint should create a charge and return the response.
app.post("/createCharge", async (req: Request, res: Response) => {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CC-Api-Key": "your_api_key_here", // Replace this with your Coinbase Commerce API Key
    },
  };

  const response = await fetch(
    "https://api.commerce.coinbase.com/charges",
    options
  );
  const data = await response.json();

  res.json(data);
});
// ---cut-after---
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

:::danger[⚠️ Warning]
Charges should only be created server-side. If you create charges on the client, users will be able to create charges associated with your Commerce Merchant account.
:::

We expose a `chargeHandler` prop on the `Checkout` component which takes a callback that is invoked every time the Checkout button is clicked.

This function **must** have the signature `() => Promise<string>` and **must** return a valid `chargeId` created by the create charge endpoint.

Note that `productId` and `chargeHandler` are mutually exclusive and only one can be provided as a prop to `Checkout`.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";

// ---cut-before---
const chargeHandler = async () => {
  // [!code focus]
  // Create a charge on your backend server using the Create Charge API // [!code focus]
  // Replace this URL with your backend endpoint // [!code focus]
  const res = await fetch("api.merchant.com/createCharge"); // [!code focus]
  const data = await res.json(); // [!code focus]
  return data.id; // Return the chargeId // [!code focus]
}; // [!code focus]

<Checkout chargeHandler={chargeHandler}>
  {" "}
  // [!code focus]
  <CheckoutButton />
</Checkout>;
// ---cut-after---
```

### Listening to the component lifecycle

You can use our Checkout [`LifecycleStatus`](/checkout/types#lifecyclestatus) and the `onStatus` prop to listen to transaction states.

```tsx twoslash
import { Checkout, CheckoutButton } from "@coinbase/onchainkit/checkout";
// ---cut-before---
import type { LifecycleStatus } from "@coinbase/onchainkit/checkout"; // [!code focus]

const statusHandler = (status: LifecycleStatus) => {
  // [!code focus]
  const { statusName, statusData } = status; // [!code focus]
  switch (
    statusName // [!code focus]
  ) {
    case "success": // [!code focus]
    // handle success
    case "pending": // [!code focus]
    // handle payment pending
    case "error": // [!code focus]
    // handle error
    default: // [!code focus]
    // handle 'init' state
  } // [!code focus]
}; // [!code focus]

<Checkout onStatus={statusHandler}>
  {" "}
  // [!code focus]
  <CheckoutButton />
</Checkout>;
// ---cut-after---
```

## Example use cases

- **Demand-based pricing:** Allow users to select seats or ticket types for events, and dynamically calculate charges based on availability and demand.
- **Product bundles:** Provide users with the option to create custom product bundles, applying discounts or special pricing based on the selected items.
- **Freelance Services:** Allow clients to specify project details such as hours, deliverables, and deadlines, and generate charges based on these custom inputs.

## Components

The components are designed to work together hierarchically. For each component, ensure the following:

- `<Checkout />` - Sets the `productId` or `chargeHandler` prop.
- `<CheckoutButton />` - Branding and customization of the payment button.
- `<CheckoutStatus />` - The status of the payment.

## Props

- [`LifecycleStatus`](/checkout/types#lifecyclestatus)
- [`CheckoutReact`](/checkout/types#checkoutreact)
- [`CheckoutButtonReact`](/checkout/types#checkoutbuttonreact)
- [`CheckoutStatusReact`](/checkout/types#checkoutstatusreact)

---

title: Checkout components & utilities Types
description: Glossary of Types in Checkout components & utilities.

---

# Types [Glossary of Types in Checkout components & utilities.]

## `LifecycleStatus`

```ts
type LifecycleStatus =
  | {
      statusName: "init";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "error";
      statusData: TransactionError;
    }
  | {
      statusName: "fetchingData";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "ready";
      statusData: {
        chargeId: string;
        contracts: ContractFunctionParameters[];
      };
    }
  | {
      statusName: "pending";
      statusData: LifecycleStatusDataShared;
    }
  | {
      statusName: "success"; // if the last mutation attempt was successful
      statusData: {
        transactionReceipts: TransactionReceipt[];
        chargeId: string;
        receiptUrl: string;
      };
    };
```

## `CheckoutButtonReact`

```ts
type CheckoutButtonReact = {
  className?: string;
  coinbaseBranded?: boolean;
  disabled?: boolean;
  icon?: React.ReactNode;
  text?: string;
};
```

## `CheckoutReact`

```ts
type CheckoutReact = {
  chargeHandler?: () => Promise<string>;
  children: React.ReactNode;
  className?: string;
  isSponsored?: boolean;
  onStatus?: (status: LifecycleStatus) => void;
  productId?: string;
};
```

## `CheckoutStatusReact`

```ts
type CheckoutStatusReact = { className?: string };
```

---

title: Farcaster utilities Types
description: Glossary of Types in Farcaster utilities.

---

# Types [Glossary of Types in Farcaster utilities.]

## `GetFarcasterUserAddressResponse`

```ts
type GetFarcasterUserAddressResponse = {
  custodyAddress?: string; // Custody Address of a given fid
  verifiedAddresses?: string[]; // List of all verified addresses for a given fid
};
```

-user-address.mdx -->

# `getFarcasterUserAddress`

The `getFarcasterUserAddress` function retrieves the user address associated
with a given Farcaster ID (fid). It provides options to specify whether
the client wants **custody address** and/or **verified addresses**,
and also allows the user to provide their own neynar api key.

By default, both **custody** and **verified** addresses are provided.

## Usage

```ts twoslash
// @noErrors: 2304 2552 - Cannot find name 'fid', Cannot find name 'options'
import { getFarcasterUserAddress } from "@coinbase/onchainkit/farcaster";

const userAddress = await getFarcasterUserAddress(fid, options); // [!code focus]
```

## Returns

[`GetFarcasterUserAddressResponse`](/farcaster/types#getfarcasteruseraddressresponse)

Returns the Custody Address and the list of all verified addresses of a given fid.

## Parameters

### fid

- **Type:** `string`

Farcaster ID

### options.neynarApiKey

- **Type:** `string`

Default to onchain-kit's default key.

```ts twoslash
// @noErrors: 2304 - Cannot find name 'fid'
import { getFarcasterUserAddress } from "@coinbase/onchainkit/farcaster";
// ---cut-before---
const userAddress = await getFarcasterUserAddress(fid, {
  neynarApiKey: "MY_NEYNAR_API_KEY", // [!code focus]
});
```

### options.hasCustodyAddress

- **Type:** `boolean`

Optional options to specify if the client wants custody addresses. Default to true.

```ts twoslash
// @noErrors: 2304 - Cannot find name 'fid'
import { getFarcasterUserAddress } from "@coinbase/onchainkit/farcaster";
// ---cut-before---
const userAddress = await getFarcasterUserAddress(fid, {
  hasCustodyAddress: false, // [!code focus]
});
```

### options.hasVerifiedAddresses

- **Type:** `boolean`

Optional options to specify if the client wants verified addresses. Default to true.

```ts twoslash
// @noErrors: 2304 - Cannot find name 'fid'
import { getFarcasterUserAddress } from "@coinbase/onchainkit/farcaster";
// ---cut-before---
const userAddress = await getFarcasterUserAddress(fid, {
  hasVerifiedAddresses: false, // [!code focus]
});
```

# Getting Started

OnchainKit is your go-to SDK for building beautiful onchain applications.

Get onchain features done faster with our pre-built components.

## Why OnchainKit?

- **Ergonomic:** Full-stack kits that simplify onchain development for all skill levels.
- **Opinionated:** Curated tools and patterns to reduce decision fatigue.
- **Use-case centric:** Pre-built components for common onchain workflows.
- **Open-source:** Transparent development with no vendor lock-in.
- **Supercharged by Base:** Leverage Base's cutting-edge protocol and ecosystem distribution.

## Automatic Installation

<img
  alt="OnchainKit Template"
  src="https://onchainkit.xyz/assets/quickstart.png"
  height="364"
/>

We recommend starting a new OnchainKit app using `create onchain`, which sets up everything automatically for you. To create a project, run:

```bash
npm create onchain@latest
```

After the prompts, `create onchain` will create a folder with your project name and install the required dependencies.

You can also checkout our pre-built templates:

- [Onchain Commerce](https://onchain-commerce-template.vercel.app/)
- [NFT minting](https://github.com/coinbase/onchain-app-template)
- [Funding flow](https://github.com/fakepixels/fund-component)
- [Social profile](https://github.com/fakepixels/ock-identity)

## Manual Installation

Add OnchainKit to your existing project manually.

::::steps

## Install OnchainKit

Install OnchainKit in your project.

:::code-group

```bash [npm]
npm install @coinbase/onchainkit
```

```bash [yarn]
yarn add @coinbase/onchainkit
```

```bash [pnpm]
pnpm add @coinbase/onchainkit
```

```bash [bun]
bun add @coinbase/onchainkit
```

:::

## Get Your Client API Key

Get your [Client API Key](https://portal.cdp.coinbase.com/projects/project-id/api-keys/client-key) from Coinbase Developer Platform.

<img
  alt="OnchainKit copy Client API Key"
  src="https://onchainkit.xyz/assets/copy-api-key-guide.png"
  height="364"
/>

Create a `.env` file in your project's root directory.

{" "}

<img
  alt="OnchainKit define Client API Key"
  src="https://onchainkit.xyz/assets/getting-started-create-env-file.png"
  width="250"
  loading="lazy"
/>

Add your Client API Key to the `.env` file:

```tsx [.env]
NEXT_PUBLIC_ONCHAINKIT_API_KEY = YOUR_CLIENT_API_KEY;
```

## Add Providers

Create a `providers.tsx` file. Add `OnchainKitProvider` as a child of `WagmiProvider` and `QueryClientProvider`.

Inside the `WagmiProvider`, wrap your app in a TanStack Query React Context Provider, e.g. `QueryClientProvider`, and pass a new `QueryClient` instance to the `client` property.

Additionally, add Base as a supported chain in the Wagmi configuration file `wagmi.ts`.

:::code-group

```tsx twoslash [providers.tsx]
// @noErrors: 2307 2580 - cannot find 'process', cannot find './wagmi'
import { OnchainKitProvider } from "@coinbase/onchainkit"; // [!code ++]
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { base } from "wagmi/chains"; // [!code ++]
import { type ReactNode, useState } from "react";
import { type State, WagmiProvider } from "wagmi";

import { getConfig } from "@/wagmi";

export function Providers(props: {
  children: ReactNode;
  initialState?: State;
}) {
  const [config] = useState(() => getConfig());
  const [queryClient] = useState(() => new QueryClient());

  return (
    <WagmiProvider config={config} initialState={props.initialState}>
      <QueryClientProvider client={queryClient}>
        <OnchainKitProvider // [!code ++]
          apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY} // [!code ++]
          chain={base} // [!code ++]
        >
          {" "}
          // [!code ++]
          {props.children}
        </OnchainKitProvider>{" "}
        // [!code ++]
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

```tsx twoslash [wagmi.ts]
import { http, cookieStorage, createConfig, createStorage } from "wagmi";
import { base } from "wagmi/chains"; // [!code ++]
import { coinbaseWallet } from "wagmi/connectors";

export function getConfig() {
  return createConfig({
    chains: [base], // [!code ++]
    connectors: [
      coinbaseWallet({
        appName: "OnchainKit",
        preference: "smartWalletOnly",
        version: "4",
      }),
    ],
    storage: createStorage({
      storage: cookieStorage,
    }),
    ssr: true,
    transports: {
      [base.id]: http(), // [!code ++]
    },
  });
}

declare module "wagmi" {
  interface Register {
    config: ReturnType<typeof getConfig>;
  }
}
```

:::

## Wrap your app with `<Providers />`

After the setup, wrap your app with the above `<Providers />` component.

```javascript
import "./globals.css";
import { Providers } from "./providers"; // [!code ++]

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode,
}>) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers> // [!code ++]
      </body>
    </html>
  );
}
```

## Add Styles

OnchainKit components come with pre-configured styles. To include these styles in your project, add the following import statement at the top of this file:

```javascript
import "@coinbase/onchainkit/styles.css";
```

For example, if you're using Next.js with the app router, your `app/layout.tsx` might look like this:

```tsx [layout.tsx]
import "@coinbase/onchainkit/styles.css"; // [!code ++]
import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { headers } from "next/headers";
import { type ReactNode } from "react";
import { cookieToInitialState } from "wagmi";

import { getConfig } from "../wagmi";
import { Providers } from "./providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Create Wagmi",
  description: "Generated by create-wagmi",
};

export default function RootLayout(props: { children: ReactNode }) {
  const initialState = cookieToInitialState(
    getConfig(),
    headers().get("cookie")
  );
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers initialState={initialState}>{props.children}</Providers>
      </body>
    </html>
  );
}
```

This ensures that the OnchainKit styles are loaded and applied to your entire application.

- For Tailwind CSS users, check out our [Tailwind Integration Guide](/guides/tailwind).

- Update the appearance of components by using our built-in themes or crafting your own custom theme.
  Explore the possibilities in our [Theming Guide](/guides/themes).

::::

## Start building!

Explore our ready-to-use onchain components:

- [**`Identity`**](/identity/identity) - Show [Basename](/identity/name), [avatars](/identity/avatar), [badges](/identity/badge), and [addresses](/identity/address).
- [**`Wallet`**](/wallet/wallet) - Create or connect wallets with [Connect Wallet](/wallet/wallet).
- [**`Transaction`**](/transaction/transaction) - Handle [transactions](/transaction/transaction) using EOAs or Smart Wallets.
- [**`Tokens`**](/token/token-chip) - Search and display [tokens](/token/token-chip) with various components.
- [**`Swap`**](/swap/swap) - Enable [token swaps](/swap/swap) in your app.
- [**`Frame`**](/frame/frame-metadata) - Build and test [Farcaster frames](/frame/frame-metadata).

onchain-app.mdx -->

---

title: Use Basename · OnchainKit
description: Integrate Basenames into your onchain app, in just a few steps.

---

import { Avatar, Name } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

# Use Basename

Basenames are an essential onchain building block that empowers builders to establish their identity on Base by registering human-readable names for their wallet addresses.

They operate entirely onchain, utilizing the same technology as ENS names, and are deployed on Base.

You can integrate [Basenames](https://www.base.org/names) into your app with few these steps.

::::steps

### New to OnchainKit?

Follow the [Getting Started](/getting-started) guide to install the package.

### Already using OnchainKit?

Update to the latest version and choose from the following steps: a React component approach, a React hook, or a pure TypeScript utility function.

::::

## React components with `<Avatar>` and `<Name>`

Use the [`<Avatar>`](/identity/avatar) and [`<Name>`](/identity/name) components to display Basenames associated with Ethereum addresses.

The `chain` prop is optional and setting to Base, it's what makes the components switch from ENS to Basenames.

```tsx twoslash
// @noErrors: 2657 - JSX expressions must have one parent element
import { Avatar, Name } from '@coinbase/onchainkit/identity';
import { base } from 'viem/chains';

const address = '0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1';

// omitted component code for brevity
<Avatar address={address} chain={base} />
<Name address={address} chain={base} />
```

<App>
  <Avatar address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" chain={base} />
  <Name address="0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1" chain={base} />
</App>

## React hooks with `useAvatar` and `useName`

Use the [`useAvatar`](/identity/use-avatar) and [`useName`](/identity/use-name) hooks to get Basenames associated with Ethereum addresses.

The hooks are incredibly useful for building custom components while leveraging OnchainKit for efficient data fetching.

:::code-group

```tsx twoslash [code]
import { useAvatar, useName } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const basename = "zizzamia.base.eth";
const { data: avatar, isLoading: avatarIsLoading } = await useAvatar({
  ensName: basename,
  chain: base,
});
const { data: name, isLoading: nameIsLoading } = await useName({
  address,
  chain: base,
});
```

```ts [return value]
{ data: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwMCIgaGVpZ2h0PSIzMDAwIiB2aWV3Qm94PSIwIDAgMzAwMCAzMDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF81NTY5XzcyODM1KSI+PHJlY3Qgd2lkdGg9IjMwMDAiIGhlaWdodD0iMzAwMCIgZmlsbD0iIzE1NURGRCIvPjxjaXJjbGUgY3g9IjE1MDAiIGN5PSIxNTAwIiByPSIxNTAwIiBmaWxsPSIjMTU1REZEIi8+PHBhdGggZD0iTTI3MTMuMTMgMTUwMEMyNzMxLjIgMTY4MC45MiAyNjE1LjEzIDE4MTguMTUgMjUwNy43OCAxOTI0LjQyQzIzOTQuNyAyMDMyLjEzIDIyOTAuNDQgMjEwOC44OCAyMjAwLjg4IDIyMDAuNjFDMjEwOS4xNSAyMjkwLjE2IDIwMzIuMjIgMjM5NC42MSAxOTI0LjUxIDI1MDcuNjhDMTgxOC4xNSAyNjE1LjA0IDE2ODAuOTIgMjczMS4xMSAxNTAwIDI3MTMuMTNDMTMxOS4wOCAyNzMxLjIgMTE4MS44NSAyNjE1LjEzIDEwNzUuNTggMjUwNy43OEM5NjcuODY2IDIzOTQuNyA4OTEuMTIgMjI5MC40NCA3OTkuMzg5IDIyMDAuODhDNzA5LjgzNyAyMTA5LjE1IDYwNS4zOSAyMDMyLjIyIDQ5Mi4zMTUgMTkyNC41MUMzODQuOTYyIDE4MTguMTUgMjY4Ljg5IDE2ODAuOTIgMjg2Ljg3MyAxNTAwQzI2OC43OTkgMTMxOS4wOCAzODQuODcxIDExODEuODUgNDkyLjIyNCAxMDc1LjU4QzYwNS4yOTkgOTY3Ljg2NiA3MDkuNTY0IDg5MS4xMiA3OTkuMTE2IDc5OS4zODlDODkwLjg0OCA3MDkuODM3IDk2Ny43NzUgNjA1LjM5IDEwNzUuNDkgNDkyLjMxNUMxMTgxLjg1IDM4NC44NzEgMTMxOS4wOCAyNjguNzk5IDE1MDAgMjg2Ljg3M0MxNjgwLjkyIDI2OC43OTkgMTgxOC4xNSAzODQuODcxIDE5MjQuNDIgNDkyLjIyNEMyMDMyLjEzIDYwNS4yOTkgMjEwOC44OCA3MDkuNTY0IDIyMDAuNjEgNzk5LjExNkMyMjkwLjE2IDg5MC44NDggMjM5NC42MSA5NjcuNzc1IDI1MDcuNjggMTA3NS40OUMyNjE1LjA0IDExODEuODUgMjczMS4xMSAxMzE5LjA4IDI3MTMuMTMgMTUwMFoiIGZpbGw9IndoaXRlIi8+PHBhdGggZD0iTTEzOTEuMDYgMTUwMEMxMzkxLjA2IDE2NDcuODkgMTM1OC40IDE3ODEuNjIgMTMwNS43NCAxODc4LjI4QzEyNTMuMDMgMTk3NS4wNSAxMTgwLjY5IDIwMzQgMTEwMS41MyAyMDM0QzEwMjIuMzYgMjAzNCA5NTAuMDMxIDE5NzUuMDUgODk3LjMxNCAxODc4LjI4Qzg0NC42NiAxNzgxLjYyIDgxMiAxNjQ3Ljg5IDgxMiAxNTAwQzgxMiAxMzUyLjExIDg0NC42NiAxMjE4LjM4IDg5Ny4zMTQgMTEyMS43MkM5NTAuMDMxIDEwMjQuOTUgMTAyMi4zNiA5NjYgMTEwMS41MyA5NjZDMTE4MC42OSA5NjYgMTI1My4wMyAxMDI0Ljk1IDEzMDUuNzQgMTEyMS43MkMxMzU4LjQgMTIxOC4zOCAxMzkxLjA2IDEzNTIuMTEgMTM5MS4wNiAxNTAwWiIgZmlsbD0iIzE1NURGRCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSI2Ii8+PGVsbGlwc2UgY3g9IjExMDIuNTciIGN5PSIxMTk0LjkzIiByeD0iMTI2LjQxNCIgcnk9IjIzMS45MzQiIGZpbGw9IndoaXRlIi8+PHBhdGggZD0iTTIxODcuMTYgMTUwMEMyMTg3LjE2IDE2NDcuODkgMjE1NC41IDE3ODEuNjIgMjEwMS44NCAxODc4LjI4QzIwNDkuMTIgMTk3NS4wNSAxOTc2Ljc5IDIwMzQgMTg5Ny42MyAyMDM0QzE4MTguNDYgMjAzNCAxNzQ2LjEzIDE5NzUuMDUgMTY5My40MSAxODc4LjI4QzE2NDAuNzYgMTc4MS42MiAxNjA4LjEgMTY0Ny44OSAxNjA4LjEgMTUwMEMxNjA4LjEgMTM1Mi4xMSAxNjQwLjc2IDEyMTguMzggMTY5My40MSAxMTIxLjcyQzE3NDYuMTMgMTAyNC45NSAxODE4LjQ2IDk2NiAxODk3LjYzIDk2NkMxOTc2Ljc5IDk2NiAyMDQ5LjEyIDEwMjQuOTUgMjEwMS44NCAxMTIxLjcyQzIxNTQuNSAxMjE4LjM4IDIxODcuMTYgMTM1Mi4xMSAyMTg3LjE2IDE1MDBaIiBmaWxsPSIjMTU1REZEIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjYiLz48ZWxsaXBzZSBjeD0iMTg5Ni41OCIgY3k9IjExOTQuOTMiIHJ4PSIxMjYuNDE0IiByeT0iMjMxLjkzNCIgZmlsbD0id2hpdGUiLz48L2c+PGRlZnM+PGNsaXBQYXRoIGlkPSJjbGlwMF81NTY5XzcyODM1Ij48cmVjdCB3aWR0aD0iMzAwMCIgaGVpZ2h0PSIzMDAwIiBmaWxsPSJ3aGl0ZSIvPjwvY2xpcFBhdGg+PC9kZWZzPjwvc3ZnPg==', isLoading: false }
{ data: 'zizzamia.base.eth', isLoading: false }
```

:::

## Typescript utility with `getAvatar` and `getName`

Use the [`getAvatar`](/identity/get-name) and [`getName`](/identity/get-name) functions to get Basenames associated with Ethereum addresses.

Being pure functions, it seamlessly integrates into any TypeScript project, including Vue, Angular, Svelte, or Node.js.

:::code-group

```tsx twoslash [code]
import { getAvatar, getName } from "@coinbase/onchainkit/identity";
import { base } from "viem/chains";

const address = "0x02feeb0AdE57b6adEEdE5A4EEea6Cf8c21BeB6B1";
const basename = "zizzamia.base.eth";
const avatar = await getAvatar({ ensName: basename, chain: base });
const name = await getName({ address, chain: base });
```

```ts [return value]
data: image / svg + xml;
base64,
  PHN2ZyB3aWR0aD0iMzAwMCIgaGVpZ2h0PSIzMDAwIiB2aWV3Qm94PSIwIDAgMzAwMCAzMDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF81NTY5XzcyODM1KSI +
    PHJlY3Qgd2lkdGg9IjMwMDAiIGhlaWdodD0iMzAwMCIgZmlsbD0iIzE1NURGRCIvPjxjaXJjbGUgY3g9IjE1MDAiIGN5PSIxNTAwIiByPSIxNTAwIiBmaWxsPSIjMTU1REZEIi8 +
    PHBhdGggZD0iTTI3MTMuMTMgMTUwMEMyNzMxLjIgMTY4MC45MiAyNjE1LjEzIDE4MTguMTUgMjUwNy43OCAxOTI0LjQyQzIzOTQuNyAyMDMyLjEzIDIyOTAuNDQgMjEwOC44OCAyMjAwLjg4IDIyMDAuNjFDMjEwOS4xNSAyMjkwLjE2IDIwMzIuMjIgMjM5NC42MSAxOTI0LjUxIDI1MDcuNjhDMTgxOC4xNSAyNjE1LjA0IDE2ODAuOTIgMjczMS4xMSAxNTAwIDI3MTMuMTNDMTMxOS4wOCAyNzMxLjIgMTE4MS44NSAyNjE1LjEzIDEwNzUuNTggMjUwNy43OEM5NjcuODY2IDIzOTQuNyA4OTEuMTIgMjI5MC40NCA3OTkuMzg5IDIyMDAuODhDNzA5LjgzNyAyMTA5LjE1IDYwNS4zOSAyMDMyLjIyIDQ5Mi4zMTUgMTkyNC41MUMzODQuOTYyIDE4MTguMTUgMjY4Ljg5IDE2ODAuOTIgMjg2Ljg3MyAxNTAwQzI2OC43OTkgMTMxOS4wOCAzODQuODcxIDExODEuODUgNDkyLjIyNCAxMDc1LjU4QzYwNS4yOTkgOTY3Ljg2NiA3MDkuNTY0IDg5MS4xMiA3OTkuMTE2IDc5OS4zODlDODkwLjg0OCA3MDkuODM3IDk2Ny43NzUgNjA1LjM5IDEwNzUuNDkgNDkyLjMxNUMxMTgxLjg1IDM4NC44NzEgMTMxOS4wOCAyNjguNzk5IDE1MDAgMjg2Ljg3M0MxNjgwLjkyIDI2OC43OTkgMTgxOC4xNSAzODQuODcxIDE5MjQuNDIgNDkyLjIyNEMyMDMyLjEzIDYwNS4yOTkgMjEwOC44OCA3MDkuNTY0IDIyMDAuNjEgNzk5LjExNkMyMjkwLjE2IDg5MC44NDggMjM5NC42MSA5NjcuNzc1IDI1MDcuNjggMTA3NS40OUMyNjE1LjA0IDExODEuODUgMjczMS4xMSAxMzE5LjA4IDI3MTMuMTMgMTUwMFoiIGZpbGw9IndoaXRlIi8 +
    PHBhdGggZD0iTTEzOTEuMDYgMTUwMEMxMzkxLjA2IDE2NDcuODkgMTM1OC40IDE3ODEuNjIgMTMwNS43NCAxODc4LjI4QzEyNTMuMDMgMTk3NS4wNSAxMTgwLjY5IDIwMzQgMTEwMS41MyAyMDM0QzEwMjIuMzYgMjAzNCA5NTAuMDMxIDE5NzUuMDUgODk3LjMxNCAxODc4LjI4Qzg0NC42NiAxNzgxLjYyIDgxMiAxNjQ3Ljg5IDgxMiAxNTAwQzgxMiAxMzUyLjExIDg0NC42NiAxMjE4LjM4IDg5Ny4zMTQgMTEyMS43MkM5NTAuMDMxIDEwMjQuOTUgMTAyMi4zNiA5NjYgMTEwMS41MyA5NjZDMTE4MC42OSA5NjYgMTI1My4wMyAxMDI0Ljk1IDEzMDUuNzQgMTEyMS43MkMxMzU4LjQgMTIxOC4zOCAxMzkxLjA2IDEzNTIuMTEgMTM5MS4wNiAxNTAwWiIgZmlsbD0iIzE1NURGRCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSI2Ii8 +
    PGVsbGlwc2UgY3g9IjExMDIuNTciIGN5PSIxMTk0LjkzIiByeD0iMTI2LjQxNCIgcnk9IjIzMS45MzQiIGZpbGw9IndoaXRlIi8 +
    PHBhdGggZD0iTTIxODcuMTYgMTUwMEMyMTg3LjE2IDE2NDcuODkgMjE1NC41IDE3ODEuNjIgMjEwMS44NCAxODc4LjI4QzIwNDkuMTIgMTk3NS4wNSAxOTc2Ljc5IDIwMzQgMTg5Ny42MyAyMDM0QzE4MTguNDYgMjAzNCAxNzQ2LjEzIDE5NzUuMDUgMTY5My40MSAxODc4LjI4QzE2NDAuNzYgMTc4MS42MiAxNjA4LjEgMTY0Ny44OSAxNjA4LjEgMTUwMEMxNjA4LjEgMTM1Mi4xMSAxNjQwLjc2IDEyMTguMzggMTY5My40MSAxMTIxLjcyQzE3NDYuMTMgMTAyNC45NSAxODE4LjQ2IDk2NiAxODk3LjYzIDk2NkMxOTc2Ljc5IDk2NiAyMDQ5LjEyIDEwMjQuOTUgMjEwMS44NCAxMTIxLjcyQzIxNTQuNSAxMjE4LjM4IDIxODcuMTYgMTM1Mi4xMSAyMTg3LjE2IDE1MDBaIiBmaWxsPSIjMTU1REZEIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjYiLz48ZWxsaXBzZSBjeD0iMTg5Ni41OCIgY3k9IjExOTQuOTMiIHJ4PSIxMjYuNDE0IiByeT0iMjMxLjkzNCIgZmlsbD0id2hpdGUiLz48L2c +
    PGRlZnM +
    PGNsaXBQYXRoIGlkPSJjbGlwMF81NTY5XzcyODM1Ij48cmVjdCB3aWR0aD0iMzAwMCIgaGVpZ2h0PSIzMDAwIiBmaWxsPSJ3aGl0ZSIvPjwvY2xpcFBhdGg +
    PC9kZWZzPjwvc3ZnPg ==
    zizzamia.base.eth;
```

:::

ps.mdx -->

---

title: Build Onchain Apps · OnchainKit
description: Our onchain app template streamlines your initial app setup and seamlessly integrates onchain components with web2 infrastructure, saving you weeks of effort.

---

# Build Onchain Apps with OnchainKit ⛵️ 🌊

Build your first onchain app effortlessly with OnchainKit's **app template**. Save weeks of initial setup
and easily integrate onchain components with web2 infrastructure.

Our opinionated approach streamlines early decisions, making your development process smoother.

Whether you're a hackathon participant or an ambitious entrepreneur aiming to build the next big thing, this template is tailored for you.

<img
  alt="Build Onchain Apps with OnchainKit"
  src="https://onchainkit.xyz/assets/onchain-app-template-1.png"
  width="702"
/>

Play with it live [here](https://onchain-app-template.vercel.app).

## Out of the box

- Next.js v14 with App routing 🏗️
- Ethereum L2 support through Base 🔵
- Easy account creation with Smart Wallet
- Live examples for Minting and Paymaster experiences with wagmi and Viem 🚀
- Latest styling best practices with Tailwind CSS 💅
- Easy maintenance with linting, formatting, and tests ✅

## Getting Started

::::steps

### Fork the repo

Go to https://github.com/coinbase/onchain-app-template and click on the "Use this template" button to create a new repository based on the template.

<img
  alt="Use OnchainKit template"
  src="https://onchainkit.xyz/assets/use-onchain-app-template.png"
  width="664"
  loading="lazy"
/>

### Client API Key(s)

Get your [Client API Key](https://portal.cdp.coinbase.com/projects/project-id/api-keys/client-key) from Coinbase Developer Platform.

<img
  alt="OnchainKit copy Client API Key"
  src="https://onchainkit.xyz/assets/copy-api-key-guide.png"
  width="664"
  loading="lazy"
/>

In order to use RainbowKit, you'd also need to obtain a Wallet Connector project ID at [WalletConnect](https://cloud.walletconnect.com/app).

### Create a .env file

Create a new file in your project’s root directory and name it `.env`.

<img
  alt="OnchainKit define Client API Key"
  src="https://onchainkit.xyz/assets/getting-started-create-env-file.png"
  width="250"
  loading="lazy"
/>

```tsx [.env]
NEXT_PUBLIC_CDP_API_KEY = YOUR_PUBLIC_API_KEY;
NEXT_PUBLIC_WC_PROJECT_ID = YOUR_WALLETCONNECT_PROJECT_ID;
```

### Install dependencies

In your new onchain app repository, run the following commands to install the dependencies:

```bash
# Install bun in case you don't have it
bun curl -fsSL <https://bun.sh/install> | bash

# Install packages
bun i
```

### Run the app

Now you are ready to run the app and start building onchain experiences!

```bash
# Run Next app
bun run dev
```

::::

## Need more help?

If you have any questions or need help, feel free to reach out to us on [Discord](https://discord.gg/vbpeXpkPkw)
or open a [Github issue](https://github.com/coinbase/onchainkit/issues) or DMs us
on X at [@onchainkit](https://x.com/onchainkit), [@zizzamia](https://x.com/zizzamia), [@fkpxls](https://x.com/fkpxls).

---

title: Tailwind CSS Integration Guide · OnchainKit
description: Learn how to integrate Tailwind CSS with OnchainKit

---

# Tailwind CSS Integration Guide

OnchainKit comes with first class support for `tailwindcss`.

::::steps

### Use default OnchainKit's style

You can use the default styles without any customization.
Just place this at the top of your application's entry point to have the components work out of the box.

```javascript
import "@coinbase/onchainkit/styles.css";
```

### Tailwind CSS Config

Depending on your dark mode setup, you may have to add `safelist: ['dark']` to your Tailwind config.

```javascript title="tailwind.config.js"
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{ts,tsx}"],
  darkMode: ["class"], // [!code focus]
  safelist: ["dark"], // [!code focus]
  theme: {
    fontFamily: {
      sans: ["Inter", "sans-serif"],
    },
  },
  plugins: [],
};
```

### Toggling light / dark mode

There are many ways to handle color mode.

In OnchainKit, toggling color mode works by adding / removing class name `dark` to the root html tag.

### Colorscheme override

To override default colorscheme, you need to modify the following css variables:

```css
@tailwind base;

@layer base {
  :root {
    --ock-font-family: "your-custom-value";
    --ock-border-radius: "your-custom-value";
    --ock-border-radius-inner: "your-custom-value";
    --ock-text-inverse: "your-custom-value";
    --ock-text-foreground: "your-custom-value";
    --ock-text-foreground-muted: "your-custom-value";
    --ock-text-error: "your-custom-value";
    --ock-text-primary: "your-custom-value";
    --ock-text-success: "your-custom-value";
    --ock-text-warning: "your-custom-value";
    --ock-text-disabled: "your-custom-value";

    --ock-bg-default: "your-custom-value";
    --ock-bg-default-hover: "your-custom-value";
    --ock-bg-default-active: "your-custom-value";
    --ock-bg-alternate: "your-custom-value";
    --ock-bg-alternate-hover: "your-custom-value";
    --ock-bg-alternate-active: "your-custom-value";
    --ock-bg-inverse: "your-custom-value";
    --ock-bg-inverse-hover: "your-custom-value";
    --ock-bg-inverse-active: "your-custom-value";
    --ock-bg-primary: "your-custom-value";
    --ock-bg-primary-hover: "your-custom-value";
    --ock-bg-primary-active: "your-custom-value";
    --ock-bg-primary-washed: "your-custom-value";
    --ock-bg-primary-disabled: "your-custom-value";
    --ock-bg-secondary: "your-custom-value";
    --ock-bg-secondary-hover: "your-custom-value";
    --ock-bg-secondary-active: "your-custom-value";
    --ock-bg-error: "your-custom-value";
    --ock-bg-warning: "your-custom-value";
    --ock-bg-success: "your-custom-value";
    --ock-bg-default-reverse: "your-custom-value";

    --ock-icon-color-primary: "your-custom-value";
    --ock-icon-color-foreground: "your-custom-value";
    --ock-icon-color-foreground-muted: "your-custom-value";
    --ock-icon-color-inverse: "your-custom-value";
    --ock-icon-color-error: "your-custom-value";
    --ock-icon-color-success: "your-custom-value";
    --ock-icon-color-warning: "your-custom-value";

    --ock-line-primary: "your-custom-value";
    --ock-line-default: "your-custom-value";
    --ock-line-heavy: "your-custom-value";
    --ock-line-inverse: "your-custom-value";
  }
}
```

::::

---

title: OnchainKit Themes · OnchainKit
description: Customize the appearance of OnchainKit's components

---

# OnchainKit Themes

<img
  alt="Themes"
  src="https://onchainkit.xyz/assets/onchainkit-themes.gif"
  height="364"
/>

## Overview

OnchainKit provides flexible appearance control through two main features: `mode` and `theme`.

- **Mode**: Controls the light/dark appearance and includes an auto option that inherits the system preference.
- **Theme**: Governs the overall styling across components.

You can choose from built-in themes or dynamically switch modes based on user preference or system settings, allowing for a customized and responsive user interface.

## Built-in Themes

OnchainKit offers multiple themes to quickly style your components. Set the theme via the `OnchainKitProvider` using `config.appearance.theme`:

- `default`: Includes both light and dark modes.
- `base`: Single mode only.
- `cyberpunk`: Single mode only.
- `hacker`: Single mode only.
- `custom`: Single mode only.

If no theme is selected, the **`default`** theme is applied automatically.

```tsx twoslash
// @noErrors:  2304 17008 1005
<OnchainKitProvider
  apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY}
  chain={base}
  config={{ // [!code focus]
    appearance: { // [!code focus]
      mode: 'auto', // 'auto' | 'light' | 'dark'
      theme: 'default', // 'default' | 'base' | 'cyberpunk' | 'hacker' // [!code focus]
    }, // [!code focus]
  }} // [!code focus]
>
```

## Mode

Control the color scheme by setting the `config.appearance.mode` property of the `OnchainKitProvider`:

- `auto`: Automatically switches between light and dark mode based on the user’s OS preference.
- `light`: Forces all components to use the light version of the theme.
- `dark`: Forces all components to use the dark version of the theme.

If no mode is specified, `auto` mode will be applied by default.

```tsx twoslash
// @noErrors:  2304 17008 1005
<OnchainKitProvider
  apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY}
  chain={base}
  config={{
    appearance: {
      mode: 'auto', // 'auto' | 'light' | 'dark' // [!code focus]
      theme: 'default', // 'default' | 'base' | 'cyberpunk' | 'hacker' | 'your-custom-theme'
    },
  }}
>
```

## CSS Overrides

Fine-tune specific aspects of an existing theme.
This is useful when you want to make adjustments to the appearance of the components without creating an entirely new theme.

```css
@layer base {
  :root .default-light,
  .default-dark,
  .base,
  .cyberpunk,
  .hacker {
    /* Override specific variables as needed */
    --ock-font-family: "your-custom-value";
    --ock-border-radius: "your-custom-value";
    --ock-text-primary: "your-custom-value";
  }
}
```

## Custom Theme

Define an entirely new look and feel for your application.
This gives you complete control over all aspects of the design, including colors, fonts, and other visual properties.

#### Usage Options:

##### Automatic Light/Dark Mode Switching:

- To automatically switch between light and dark versions of your custom theme:

```tsx twoslash
// @noErrors:  2304 17008 1005
<OnchainKitProvider
  apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY}
  chain={base}
  config={{
    appearance: {
      mode: 'auto', // [!code focus]
      theme: 'custom', // [!code focus]
    },
  }}
>
```

##### Single Theme Version:

- To use only one version of your custom theme at all times:

```tsx twoslash
// @noErrors:  2304 17008 1005
<OnchainKitProvider
  apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY}
  chain={base}
  config={{
    appearance: {
      mode: 'light', // [!code focus]
      theme: 'custom', // [!code focus]
    },
  }}
>
```

##### Defining a custom theme

Use CSS variables to define your custom theme.
The class name definitions must include the `-light` or `-dark` suffix.

```css
@layer base {
  .custom-light {
    /* Font and Shape */
    --ock-font-family: "your-custom-value";
    --ock-border-radius: "your-custom-value";
    --ock-border-radius-inner: "your-custom-value";

    /* Text Colors */
    --ock-text-inverse: "your-custom-value";
    --ock-text-foreground: "your-custom-value";
    --ock-text-foreground-muted: "your-custom-value";
    --ock-text-error: "your-custom-value";
    --ock-text-primary: "your-custom-value";
    --ock-text-success: "your-custom-value";
    --ock-text-warning: "your-custom-value";
    --ock-text-disabled: "your-custom-value";

    /* Background Colors */
    --ock-bg-default: "your-custom-value";
    --ock-bg-default-hover: "your-custom-value";
    --ock-bg-default-active: "your-custom-value";
    --ock-bg-alternate: "your-custom-value";
    --ock-bg-alternate-hover: "your-custom-value";
    --ock-bg-alternate-active: "your-custom-value";
    --ock-bg-inverse: "your-custom-value";
    --ock-bg-inverse-hover: "your-custom-value";
    --ock-bg-inverse-active: "your-custom-value";
    --ock-bg-primary: "your-custom-value";
    --ock-bg-primary-hover: "your-custom-value";
    --ock-bg-primary-active: "your-custom-value";
    --ock-bg-primary-washed: "your-custom-value";
    --ock-bg-primary-disabled: "your-custom-value";
    --ock-bg-secondary: "your-custom-value";
    --ock-bg-secondary-hover: "your-custom-value";
    --ock-bg-secondary-active: "your-custom-value";
    --ock-bg-error: "your-custom-value";
    --ock-bg-warning: "your-custom-value";
    --ock-bg-success: "your-custom-value";
    --ock-bg-default-reverse: "your-custom-value";

    /* Icon Colors */
    --ock-icon-color-primary: "your-custom-value";
    --ock-icon-color-foreground: "your-custom-value";
    --ock-icon-color-foreground-muted: "your-custom-value";
    --ock-icon-color-inverse: "your-custom-value";
    --ock-icon-color-error: "your-custom-value";
    --ock-icon-color-success: "your-custom-value";
    --ock-icon-color-warning: "your-custom-value";

    /* Line Colors */
    --ock-line-primary: "your-custom-value";
    --ock-line-default: "your-custom-value";
    --ock-line-heavy: "your-custom-value";
    --ock-line-inverse: "your-custom-value";
  }

  .custom-dark {
    /* Define dark mode custom classes here */
  }
}
```

.mdx -->

---

title: Lifecycle Status · OnchainKit
description: How to influences the behavior of your components and onchain data with Lifecycle Status.

---

# Lifecycle Status

OnchainKit Lifecycle Status allows you to manage the state of APIs and onchain transactions seamlessly within components.

## How to listen to the Lifecycle status

The Lifecycle Status is a TypeScript object that provides easy access to the `statusName` and `statusData` properties,
allowing you to stay informed and responsive.

```tsx twoslash
import { useCallback } from "react";
import { Transaction } from "@coinbase/onchainkit/transaction";
// ---cut-before---
import type { LifecycleStatus } from "@coinbase/onchainkit/transaction";

const handleOnStatus = useCallback((status: LifecycleStatus) => {
  console.log("LifecycleStatus", status);
}, []);

<Transaction onStatus={handleOnStatus}>
  // omitted component code for brevity
</Transaction>;
```

## Lifecycle Status

The Lifecycle Status includes 3 states common to all components:

### `init`

The component is initialized and ready for use.

```ts
{
  statusName: "init";
  statusData: null;
}
```

### `success`

The component has successfully completed its main action, such as `swap` or `transaction`.

```ts
{
  statusName: "success";
  statusData: {
    // the data returned from the API or onchain operation
  }
}
```

### `error`

The component has encountered an issue while fetching API data, executing an onchain operation,
or needs to display a visual message to the user.

```ts
{
  statusName: "error";
  statusData: {
    code: string; // The error code representing the location of the error
    error: string; // The error message providing developer details
    message: string; // The error message providing user-facing details
  }
}
```

<br />

Each component brings its own unique experience, and we have explored both the swap and transaction processes.

## Lifecycle Status with [`<Swap />`](/swap/swap)

### `amountChange`

Any of the Swap Input fields have been updated.

```ts
{
  statusName: 'amountChange';
  statusData: {
    amountFrom: string;
    amountTo: string;
    tokenFrom?: Token;
    tokenTo?: Token;
    isMissingRequiredField: boolean;
  };
}
```

### `transactionPending`

The transaction has been submitted to the network but has not yet been confirmed to be included in a block.
During this pending state, the transaction is waiting to be validated by the network's consensus mechanism.

```ts
{
  statusName: "transactionPending";
  statusData: null;
}
```

### `transactionApproved`

The transaction has been verified to be valid and it has been included in a block
however the transaction is not yet finalized.

```ts
{
  statusName: "transactionApproved";
  statusData: {
    transactionHash: Hex;
    transactionType: "Batched" | "ERC20" | "Permit2" | "Swap";
  }
}
```

### `success`

The transaction has been added to the blockchain and the transaction is considered final.

```ts
{
  statusName: "success";
  statusData: {
    transactionReceipt: TransactionReceipt;
  }
}
```

## Lifecycle Status with [`<Transaction />`](/transaction/transaction)

### `transactionIdle`

The transaction component is waiting for the user to take action.

```ts
{
  statusName: "transactionIdle";
  statusData: null;
}
```

### `transactionPending`

The transaction has been submitted to the network but has not yet been confirmed to be included in a block.
During this pending state, the transaction is waiting to be validated by the network's consensus mechanism.

```ts
{
  statusName: "transactionPending";
  statusData: null;
}
```

### `success`

The transaction has been added to the blockchain and the transaction is considered final.

```ts
{
  statusName: 'success';
  statusData: {
    transactionReceipts: TransactionReceipt[];
  };
}
```

>

# Framegear

**Framegear** is a simple tool that allows you to run and test your frames locally:

- without publishing
- without casting
- without spending warps

## Installation and Usage

**Framegear** is currently distributed as part of the [@coinbase/onchainkit](https://github.com/coinbase/onchainkit) Git repository.

:::code-group

```bash [npm]
git clone https://github.com/coinbase/onchainkit.git

cd onchainkit/framegear
npm install
npm run dev
```

```bash [yarn]
git clone https://github.com/coinbase/onchainkit.git

cd onchainkit/framegear
yarn
yarn dev
```

```bash [pnpm]
git clone https://github.com/coinbase/onchainkit.git

cd onchainkit/framegear
pnpm install
pnpm run dev
```

```bash [bun]
git clone https://github.com/coinbase/onchainkit.git

cd onchainkit/framegear
bun install
bun run dev
```

:::

Visit http://localhost:1337 to start the **Framegear** interface. Enter the URL of your locally
running frame (e.g., `http://localhost:3000`) and click `Fetch` to validate your frame response and start testing.

![Fetch Frame](https://onchainkit.xyz/assets/fetch-frame.png)

### Frame-specific setup

**Framegear** can validate the initial response of any frame. For more advanced debugging capabilities,
consider building the frame using `@coinbase/onchainkit` (versions `^0.8.0`). When using the `getFrameMessage` function,
include the `allowFramegear` option to enable **Framegear** to send mock frame actions.

```ts twoslash
// @noErrors: 2304 - Cannot find 'body'
import { getFrameMessage } from "@coinbase/onchainkit/frame";

// ...

const { isValid, message } = await getFrameMessage(body, {
  allowFramegear: true, // [!code focus]
});
```

### Security Tip

When setting up frames in production, remember not to include the `allowFramegear` option.
The exact setup might vary based on the application, but here's one example:

```ts twoslash
// @noErrors: 2580 2304 - Cannot find 'process', Cannot find 'body'
import { getFrameMessage } from "@coinbase/onchainkit/frame";

const allowFramegear = process.env.NODE_ENV !== "production"; // [!code focus]

// ...

const { isValid, message } = await getFrameMessage(body, {
  allowFramegear, // [!code focus]
});
```

## Current Abilities

At present, **Framegear** is able to validate the initial frame response against the
[current Frame Specification](https://docs.farcaster.xyz/reference/frames/spec) and interact with frames through
buttons using the `post` action.

**Framegear** is under active development and much more functionality is on the roadmap including (but not limited to):

- more button actions
- text input
- simulated conditions
  - viewer followed
  - viewer liked
  - viewer recasted

A partial roadmap can be viewed at https://github.com/coinbase/onchainkit/issues/146

-->

---

title: Contribution Guide · OnchainKit
description: Learn how to contribute to OnchainKit

---

# Contribution Guide

Welcome to OnchainKit! So you want to contribute to this project? You came to the right place.

In this guide, you will learn how to:

- [Set up this project](#setup)
- [Navigate the codebase](#codebase)
- [Accomplish various workflows](#workflows)
- [Submit feature request](#feature-request)

## Setup

### Clone this repo

```bash
git clone git@github.com:coinbase/onchainkit.git
```

### Install node + yarn

Use nvm, mise, n or whatever works for you. Once node is installed, run this to enable yarn:

```bash
corepack enable
```

### Install dependencies

```bash
cd onchainkit

yarn install
```

## Codebase

Here is a rough layout of this codebase:

```bash
onchainkit
├── src
│   ├── core/                     - Files with zero dependencies
│   ├── token/                    - Token
│   │   ├── components/           - React components
│   │   │   ├── {Name}.tsx
│   │   │   ├── {Name}.test.tsx
│   │   │   └── {Name}.css
│   │   ├── core/                 - Utility functions
│   │   ├── index.ts              - Entrypoint for the folder
│   │   └── types.ts              - Export types
│   │  
│   ├── index.ts                  - Typescript entrypoint
│   ├── index.css                 - CSS entrypoint
│   └── OnchainKitProvider.tsx    - OnchainKit provider
└── site/
    ├── sidebar.ts                - Controls sidebar for the doc site
    └── docs/pages/**/*.mdx       - Documentation location
```

## Workflows

### Docs

We use [Vocs](https://vocs.dev) to power this site. Vocs includes support for [twoslash](https://vocs.dev/docs/guides/twoslash) to display types in code blocks on an opt-in basis.

To enable twoslash in any ts/tsx code block you can add twoslash after your code block declaration, i.e. &grave;&grave;&grave;tsx twoslash

If your codeblock is not valid, you will see errors generated from twoslash. If you cannot resolve these errors in code, it is possible to suppress twoslash using the [noErrors](https://vocs.dev/docs/guides/twoslash#noerrors) syntax.

```
// @noErrors: 2304 - Cannot find name
```

### Storybook

Storybook is a frontend workshop for building UI components and pages in isolation. It helps you develop and share hard-to-reach states and edge cases without needing to run your whole app.

To develop and test your components in Storybook, run the following command:

```bash
yarn storybook:dev

# In a browser, navigate to http://localhost:6006/
```

### Testing

Write and update existing unit tests. You can watch file changes and rerun tests automatically like this:

```bash
yarn test --watch
```

We expect 100% code coverage for any updates. You can get coverage information with:

```bash
yarn test:coverage
```

If the coverage drops below 100%, look at the coverage report generated by the above command with:

```bash
open coverage/index.html
```

### Testing UI with hotreload

We use this doc site to test UI changes.

Navigate to the markdown used for the given file you are updating (i.e. `site/docs/pages/identity/avatar.mdx`)
and change the import using relative import path like this:

```mdx
import { Avatar } from "../../../../src/identity";

;
```

To bring up the doc site, run:

```bash
cd site

yarn install

yarn dev

# In a browser, navigate to http://localhost:5173
```

Your changes should automatically reflect in the doc site

### Updating changelog

To update the change log, run:

```bash
yarn changeset
```

Select `minor` and use the following format for the summary:

```markdown
- **feat**: feature update information. By @your-github-id #XX (XX is the PR number)
```

Use possible values are:

- `feat`
- `fix`
- `docs`
- `chore`

## Feature request

Have a component in mind that we are not supporting yet? You can submit a feature request to our [Github](https://github.com/coinbase/onchainkit/issues). Create a **"New issue"** and label it "Feature Request: ..."

x -->

---

title: Reporting a bug · OnchainKit
description: Help us make OnchainKit better

---

# OnchainKit Bug Reporting Guide

Welcome to OnchainKit!

We look at all of your bug reports and will do our best to fix them as quickly as possible.

::::steps

### Create a new issue

Navigate to [Issues tab](https://github.com/coinbase/onchainkit/issues) on Github and click the "New issue" button.

### Select "Bug Report"

Pick the "Bug Report" option and fill out the form to the best of your ability.

### We'll be in touch

We'll do our best to respond to your issue on Github as soon as possible.
::::

### Have a special request?

You can tag us on [Discord](https://discord.com/channels/1220414409550336183/1253768005863739565) or DM us on [X](https://x.com/Onchainkit).

We're most active on Github, so if you're able to, please create an issue there.

fund-link.mdx -->

---

title: Wallet Components & Utilities · OnchainKit
description: Introduction to Wallet Components & Utilities

---

import {
ConnectWallet,
Wallet,
WalletDropdown,
WalletDropdownFundLink,
WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import {
Address,
Avatar,
Name,
Identity,
EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import WalletComponents from "../../components/WalletComponents";
import { walletDropdownLinkCustomBaseIconSvg } from "../../components/svg/walletDropdownLinkCustomBaseIconSvg";

# `<WalletDropdownFundLink />`

The `WalletDropdownFundLink` works just like the [`FundButton`](/fund/fund-button) except that it's inside your wallet
dropdown menu.

If your user connects a Coinbase Smart Wallet, it provides an easy way to access the Coinbase Smart Wallet
[Fund](https://keys.coinbase.com/fund) flow. Users will be able to buy and receive crypto, or use their Coinbase
balances onchain with [Magic Spend](https://www.smartwallet.dev/guides/magic-spend).

If your user connects any other EOA wallet, it provides an easy way to access [Coinbase Onramp](https://docs.cdp.coinbase.com/onramp/docs/welcome/)
where your users will also be able to buy crypto using a fiat payment method, or transfer existing crypto from their
Coinbase account.

:::tip[Coinbase Onramp Support]
If you would like to provide non Coinbase Smart Wallet users with an easy way to access Coinbase Onramp, please make
sure you go through the `FundButton` [walkthrough](/fund/fund-button#walkthrough) to configure your Project ID. Otherwise
only Coinbase Smart Wallet users will be able to use the `WalletDropdownFundLink`.
:::

## Usage

```tsx twoslash
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownDisconnect,
  WalletDropdownFundLink, // [!code focus]
} from "@coinbase/onchainkit/wallet"; // [!code focus]
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";

export function WalletComponents() {
  return (
    <div className="flex justify-end">
      <Wallet>
        <ConnectWallet>
          <Avatar className="h-6 w-6" />
          <Name />
        </ConnectWallet>
        <WalletDropdown>
          <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
            <Avatar />
            <Name />
            <Address />
            <EthBalance />
          </Identity>
          <WalletDropdownFundLink /> // [!code focus]
          <WalletDropdownDisconnect />
        </WalletDropdown>
      </Wallet>
    </div>
  );
}
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownFundLink />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override text

You can override component text using the `text` prop.

```tsx
<WalletDropdownFundLink text="Add crypto" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <WalletDropdownFundLink text="Add crypto" />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override icon

You can override the icon using the `icon` prop.

```tsx
<WalletDropdownFundLink icon={baseIcon} /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <WalletDropdownFundLink icon={walletDropdownLinkCustomBaseIconSvg} />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Customizing the popup size

You're able to customize the size of the popup window using the `popupSize` prop. Valid values are `sm`, `md`, and `lg`.

```tsx
<WalletDropdownFundLink popupSize="sm" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <WalletDropdownFundLink popupSize="sm" />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override default behavior

You can override default link behavior by using the `openIn` prop. Valid values are `popup` and `tab`.

```tsx
<WalletDropdownFundLink openIn="tab" target="_blank" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <WalletDropdownFundLink openIn="tab" target="_blank" />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override funding URL

You can override the default URL by using the `fundingUrl` prop.

```tsx
<WalletDropdownFundLink
  fundingUrl={"https://base.org"}
  openIn="tab"
  target="_blank"
/> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <WalletDropdownFundLink
        fundingUrl={"https://base.org"}
        openIn="tab"
        target="_blank"
      />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

## Props

- [`WalletDropdownFundLinkReact`](/wallet/types#walletdropdownfundlinkreact)

disconnect.mdx -->

import {
Address,
Avatar,
Name,
Identity,
EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
ConnectWallet,
Wallet,
WalletDropdown,
WalletDropdownLink,
WalletDropdownBasename,
WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import WalletComponents from "../../components/WalletComponents";

# `<WalletDropdownDisconnect />`

The `WalletDropdownDisconnect` component is used to disconnect the wallet from the application.

## Usage

```tsx twoslash
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownDisconnect, // [!code focus]
} from "@coinbase/onchainkit/wallet";

export function WalletComponents() {
  return (
    <div className="flex justify-end">
      <Wallet>
        <ConnectWallet>
          <Avatar className="h-6 w-6" />
          <Name />
        </ConnectWallet>
        <WalletDropdown>
          <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
            <Avatar />
            <Name />
            <Address className={color.foregroundMuted} />
            <EthBalance />
          </Identity>
          <WalletDropdownDisconnect /> // [!code focus]
        </WalletDropdown>
      </Wallet>
    </div>
  );
}
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override styles

You can override component styles using `className`.

```tsx
// omitted for brevity

<WalletDropdownDisconnect className="hover:bg-red-500" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet text="Log In">
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownDisconnect className="hover:bg-red-500" />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override text

You can override component text using `text`.

```tsx
// omitted for brevity

<WalletDropdownDisconnect text="Log out" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet text="Log In">
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownDisconnect text="Log out" />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

## Props

- [`WalletDropdownDisconnectReact`](/wallet/types#walletdropdowndisconnectreact)

---

title: <Wallet /> · OnchainKit
description: The `<Wallet />` components provide an interface for users to connect their Smart Wallet with their identity information like Basename and ETH balance.

---

import {
ConnectWallet,
ConnectWalletText,
Wallet,
WalletDefault,
WalletDropdown,
WalletDropdownBasename,
WalletDropdownFundLink,
WalletDropdownLink,
WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import {
Address,
Avatar,
Name,
Identity,
EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import AppWithRK from "../../components/AppWithRK";
import WalletComponents from "../../components/WalletComponents";

# `<Wallet />`

The `<Wallet />` components provide an interface for users to connect their
Smart Wallet with their identity information like Basename and ETH balance.

It features built-in polished user experiences for both web and mobile web,
making it incredibly easy to enhance with drop-in components.

Before using them, ensure you've completed all [Getting Started steps](/getting-started).

## Quick start

The `WalletDefault` component is a simplified version of the `Wallet` component, designed to streamline the integration process for developers. Instead of manually defining each subcomponent and prop, developers can use this shorthand version which renders our suggested implementation of the component.

If you'd like more customization, follow the implementation guide for our `Wallet` component below.

```tsx twoslash
import { WalletDefault } from "@coinbase/onchainkit/wallet";

export function WalletComponents() {
  return (
    // ---cut-before---
    // omitted for brevity

    <WalletDefault /> // [!code focus]
    // ---cut-after---
  );
}
```

<WalletComponents>
  <WalletDefault />
</WalletComponents>

## Walkthrough

::::steps

### Set up your wallet connections

Kick off your wallet connection setup by configuring the `wagmi` provider.

And make sure to update the `appName` as that will be displayed to
the user when they connect their wallet.

```tsx twoslash
import { ReactNode } from "react";
import { WagmiProvider, createConfig, http } from "wagmi";
import { baseSepolia } from "wagmi/chains";
import { coinbaseWallet } from "wagmi/connectors";

const wagmiConfig = createConfig({
  chains: [baseSepolia],
  connectors: [
    coinbaseWallet({
      appName: "onchainkit",
    }),
  ],
  ssr: true,
  transports: {
    [baseSepolia.id]: http(),
  },
});

function App({ children }: { children: ReactNode }) {
  return <WagmiProvider config={wagmiConfig}>{children}</WagmiProvider>;
}
```

### Drop in the `<Wallet />` components

Experience the magic by simply dropping in the `<Wallet />` component
and watch it seamlessly come to life.

<br />
Additionally, you can see the [`<Identity>`](/identity/identity) components 
like [`<Avatar>`](/identity/avatar), [`<Name>`](/identity/name), 
and [`<Address>`](/identity/address) are used in a composable way. 
Explore their documentation pages to discover various customization options.

```tsx twoslash
import {
  // [!code focus]
  ConnectWallet, // [!code focus]
  Wallet, // [!code focus]
  WalletDropdown, // [!code focus]
  WalletDropdownDisconnect, // [!code focus]
} from "@coinbase/onchainkit/wallet"; // [!code focus]
import { Address, Avatar, Name, Identity } from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";

export function WalletComponents() {
  return (
    <div className="flex justify-end">
      <Wallet>
        {" "}
        // [!code focus]
        <ConnectWallet>
          {" "}
          // [!code focus]
          <Avatar className="h-6 w-6" />
          <Name />
        </ConnectWallet>{" "}
        // [!code focus]
        <WalletDropdown>
          {" "}
          // [!code focus]
          <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
            <Avatar />
            <Name />
            <Address className={color.foregroundMuted} />
          </Identity>
          <WalletDropdownDisconnect /> // [!code focus]
        </WalletDropdown> // [!code focus]
      </Wallet>{" "}
      // [!code focus]
    </div>
  );
}
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
      </Identity>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Drop in pre-made wallet components

Expand the user experience with pre-made components like [`<WalletDropdownLink>`](/wallet/wallet-dropdown-link),
[`<WalletDropdownBasename>`](/wallet/wallet-dropdown-basename),
[`<WalletDropdownFundLink>`](/wallet/wallet-dropdown-fund-link),
or `<EthBalance>`, to help you build a seamless wallet experience for your users.

<br />
The `<WalletDropdownLink>` is highly versatile and will likely be your go-to choice 
for adding more links to the dropdown, connecting your users to various pages of your onchain app.

```tsx twoslash
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownBasename, // [!code focus]
  WalletDropdownFundLink, // [!code focus]
  WalletDropdownLink, // [!code focus]
  WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance, // [!code focus]
} from "@coinbase/onchainkit/identity";

// omitted for brevity

<Wallet>
  <ConnectWallet>
    <Avatar className="h-6 w-6" />
    <Name />
  </ConnectWallet>
  <WalletDropdown>
    <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
      <Avatar />
      <Name />
      <Address />
      <EthBalance /> // [!code focus]
    </Identity>
    <WalletDropdownBasename /> // [!code focus]
    <WalletDropdownLink // [!code focus]
      icon="wallet" // [!code focus]
      href="https://keys.coinbase.com" // [!code focus]
    >
      {" "}
      // [!code focus] Wallet // [!code focus]
    </WalletDropdownLink>{" "}
    // [!code focus]
    <WalletDropdownFundLink /> // [!code focus]
    <WalletDropdownDisconnect />
  </WalletDropdown>
</Wallet>;
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownBasename />
      <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
        Wallet
      </WalletDropdownLink>
      <WalletDropdownFundLink />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Customize Connect button text and style

Each OnchainKit component offers the flexibility to customize `className`
and adjust the style of the React components it represents.

Customize the connect wallet text by using directly the `<ConnectWalletText>` component.

```tsx twoslash
import {
  ConnectWallet,
  ConnectWalletText,
  Wallet,
  WalletDropdown,
  WalletDropdownLink,
  WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
// ---cut-before---
// omitted for brevity

<Wallet>
  <ConnectWallet className="bg-blue-800">
    {" "}
    // [!code focus]
    <ConnectWalletText>Log In</ConnectWalletText> // [!code focus]
    <Avatar className="h-6 w-6" /> // [!code focus]
    <Name className="text-white" /> // [!code focus]
  </ConnectWallet>
  <WalletDropdown>
    <Identity
      className="px-4 pt-3 pb-2 hover:bg-blue-200" // [!code focus]
      hasCopyAddressOnClick
    >
      <Avatar />
      <Name />
      <Address />
      <EthBalance />
    </Identity>
    <WalletDropdownLink
      className="hover:bg-blue-200" // [!code focus]
      icon="wallet"
      href="https://keys.coinbase.com"
    >
      Wallet
    </WalletDropdownLink>
    <WalletDropdownDisconnect className="hover:bg-blue-200" /> // [!code focus]
  </WalletDropdown>
</Wallet>;
```

<WalletComponents>
  <Wallet>
    <ConnectWallet className="bg-blue-800">
      <ConnectWalletText>Log In</ConnectWalletText>
      <Avatar className="h-6 w-6" />
      <Name className="text-white" />
    </ConnectWallet>
    <WalletDropdown>
      <Identity
        className="px-4 pt-3 pb-2 hover:bg-blue-200"
        hasCopyAddressOnClick
      >
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownLink
        className="hover:bg-blue-200"
        icon="wallet"
        href="https://keys.coinbase.com"
      >
        Wallet
      </WalletDropdownLink>
      <WalletDropdownDisconnect className="hover:bg-blue-200" />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Use RainbowKit for wallet aggregation

You can expand the wallet connection options by using the `withWalletAggregator` prop in the `<ConnectWallet />` component. This will present users with a list of recommended and other wallets to choose from.

OnchainKit leverages [RainbowKit](https://www.rainbowkit.com/) to offer this feature. To use it correctly, follow these steps:

1. Import the necessary components from RainbowKit.
2. Create a list of recommended and other wallets.
3. Use `getDefaultConfig` to configure the Wagmi provider.
4. Wrap your app in the RainbowKit provider.

:::code-group

```tsx twoslash [myApp.tsx]
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownLink,
  WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
// ---cut-before---
// omitted for brevity

<Wallet>
  <ConnectWallet withWalletAggregator>
    {" "}
    // [!code focus]
    <Avatar className="h-6 w-6" />
    <Name />
  </ConnectWallet>
  <WalletDropdown>
    <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
      <Avatar />
      <Name />
      <Address />
      <EthBalance />
    </Identity>
    <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
      Wallet
    </WalletDropdownLink>
    <WalletDropdownDisconnect />
  </WalletDropdown>
</Wallet>;
```

```tsx twoslash [OnchainProviders.tsx]
// @noErrors: 2304 2322 - Cannot find VITE_WALLET_CONNECT_PROJECT_ID, Canoot find name Props
"use client";
import type { ReactNode } from "react";
import { OnchainKitProvider } from "@coinbase/onchainkit";
import {
  // [!code focus]
  RainbowKitProvider, // [!code focus]
  connectorsForWallets, // [!code focus]
  getDefaultConfig, // [!code focus]
} from "@rainbow-me/rainbowkit"; // [!code focus]
import {
  // [!code focus]
  metaMaskWallet, // [!code focus]
  rainbowWallet, // [!code focus]
  coinbaseWallet, // [!code focus]
} from "@rainbow-me/rainbowkit/wallets"; // [!code focus]
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { WagmiProvider } from "wagmi";
import { base } from "wagmi/chains";

import "@coinbase/onchainkit/styles.css";
import "@rainbow-me/rainbowkit/styles.css"; // [!code focus]

const queryClient = new QueryClient();

const connectors = connectorsForWallets(
  // [!code focus]
  [
    {
      groupName: "Recommended Wallet",
      wallets: [coinbaseWallet],
    },
    {
      groupName: "Other Wallets",
      wallets: [rainbowWallet, metaMaskWallet],
    },
  ],
  {
    appName: "onchainkit",
    projectId: VITE_WALLET_CONNECT_PROJECT_ID,
  }
); // [!code focus]

const wagmiConfig = getDefaultConfig({
  // [!code focus]
  appName: "onchainkit",
  connectors,
  projectId: process.env.PUBLIC_WALLET_CONNECT_PROJECT_ID,
  chains: [base],
  ssr: true, // If your dApp uses server side rendering (SSR)
}); // [!code focus]

function OnchainProviders({ children }: Props) {
  return (
    <WagmiProvider config={wagmiConfig}>
      <QueryClientProvider client={queryClient}>
        <OnchainKitProvider
          apiKey={process.env.PUBLIC_ONCHAINKIT_API_KEY}
          chain={base}
        >
          <RainbowKitProvider modalSize="compact">
            {" "}
            // [!code focus]
            {children}
          </RainbowKitProvider>{" "}
          // [!code focus]
        </OnchainKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}

export default OnchainProviders;
```

:::

<AppWithRK>
  <div className="my-10 flex justify-center">
    <Wallet>
      <ConnectWallet withWalletAggregator>
        <Avatar className="h-6 w-6" />
        <Name />
      </ConnectWallet>
      <WalletDropdown>
        <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
          <Avatar />
          <Name />
          <Address className={color.foregroundMuted} />
          <EthBalance />
        </Identity>
        <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
          Wallet
        </WalletDropdownLink>
        <WalletDropdownDisconnect />
      </WalletDropdown>
    </Wallet>
  </div>
</AppWithRK>

::::

## Components

The components are designed to work together hierarchically. For each component, ensure the following:

- `<Wallet />` - Serves as the main container for all wallet-related components.
- `<ConnectWallet />` - Handles the wallet connection process. Place child components inside to customize the connect button appearance.
- `<WalletDropdown />` - Contains additional wallet information and options. Place inside the `<Wallet />` component.
- `<Identity />` - Displays user identity information. Place inside `<WalletDropdown />` for a complete profile view.
- `<WalletDropdownBasename />` - Displays the user's Basename within the dropdown.
- `<WalletDropdownLink />` - Creates a custom link within the dropdown. Use the `icon` prop to add an icon, and `href` to specify the destination.
- `<WalletDropdownDisconnect />` - Provides a disconnect option within the dropdown.

Additional components for customizing the wallet interface include:

- `<Avatar />` - Displays the user's avatar image.
- `<Name />` - Shows the user's name or ENS.
- `<Badge />` - Can be used to display additional user status or information.
- `<Address />` - Shows the user's wallet address.
- `<EthBalance />` - Displays the user's ETH balance.

The Wallet component automatically handles the wallet connection state and updates the UI accordingly.
You need to wrap your application or relevant part of it with these components
to provide a complete wallet interaction experience.

## Component types

- [`WalletReact`](/wallet/types#walletreact)
- [`ConnectWalletReact`](/wallet/types#connectwalletreact)
- [`WalletDropdownReact`](/wallet/types#walletdropdownreact)
- [`WalletDropdownBasenameReact`](/wallet/types#walletdropdownbasenamereact)
- [`WalletDropdownDisconnectReact`](/wallet/types#walletdropdowndisconnectreact)
- [`WalletDropdownLinkReact`](/wallet/types#walletdropdownlinkreact)

link.mdx -->

import {
Address,
Avatar,
EthBalance,
Identity,
Name,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
ConnectWallet,
Wallet,
WalletDropdown,
WalletDropdownBasename,
WalletDropdownDisconnect,
WalletDropdownLink,
} from "@coinbase/onchainkit/wallet";
import WalletComponents from "../../components/WalletComponents";
import { walletDropdownLinkCustomBaseIconSvg } from "../../components/svg/walletDropdownLinkCustomBaseIconSvg";

# `<WalletDropdownLink />`

The `WalletDropdownLink` component creates customizable, interactive links within the wallet dropdown menu.

## Usage

```tsx twoslash
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownLink, // [!code focus]
  WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";

export function WalletComponents() {
  return (
    <div className="flex justify-end">
      <Wallet>
        <ConnectWallet>
          <Avatar className="h-6 w-6" />
          <Name />
        </ConnectWallet>
        <WalletDropdown>
          <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
            <Avatar />
            <Name />
            <Address className={color.foregroundMuted} />
            <EthBalance />
          </Identity>
          <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
            {" "}
            // [!code focus] Wallet // [!code focus]
          </WalletDropdownLink> // [!code focus]
          <WalletDropdownDisconnect />
        </WalletDropdown>
      </Wallet>
    </div>
  );
}
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
        Wallet
      </WalletDropdownLink>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Custom link

Add a custom link to the wallet dropdown menu, allowing users to navigate to external resources directly from the wallet interface.

```tsx twoslash
// @noErrors: 2304 Cannot find name 'BaseIcon'
import { WalletDropdownLink } from "@coinbase/onchainkit/wallet";
// ---cut-before---
// omitted for brevity
<WalletDropdownLink // [!code focus]
  icon={BaseIcon} // [!code focus]
  href="https://www.base.org/" // [!code focus]
  rel="noopener noreferrer" // [!code focus]
>
  {" "}
  // [!code focus] Base.org // [!code focus]
</WalletDropdownLink>; // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownLink
        icon={walletDropdownLinkCustomBaseIconSvg}
        href="https://www.base.org/"
        rel="noopener noreferrer"
      >
        Base.org
      </WalletDropdownLink>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Custom children components

Accepts React children, enabling the use of custom elements, styled text, icons, and complex components.
This allows for diverse customizations, including complex layouts and conditional rendering based on your app's state.

```tsx twoslash
// @noErrors: 2322 - type 'Element' is not assignable to type 'string'
import { WalletDropdownLink } from "@coinbase/onchainkit/wallet";
// ---cut-before---
// omitted for brevity
<WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
  {" "}
  // [!code focus]
  <span className="font-bold italic">Profile</span> // [!code focus]
  <span> 🔵 </span> // [!code focus]
</WalletDropdownLink>; // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownLink icon="wallet" href="https://keys.coinbase.com">
        <span className="font-bold italic">Profile</span>
        <span> 🔵 </span>
      </WalletDropdownLink>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override styles

You can override component styles using className.

```tsx twoslash
import { WalletDropdownLink } from "@coinbase/onchainkit/wallet";
// ---cut-before---
// omitted for brevity
<WalletDropdownLink
  className="hover:bg-red-500"
  icon="wallet"
  href="https://keys.coinbase.com"
>
  {" "}
  // [!code focus] Wallet // [!code focus]
</WalletDropdownLink>; // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet>
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownLink
        className="hover:bg-red-500"
        icon="wallet"
        href="https://keys.coinbase.com"
      >
        Wallet
      </WalletDropdownLink>
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

## Props

- [`WalletDropdownLinkReact`](/wallet/types#walletdropdownlinkreact)

ypoint.mdx -->

# `isValidAAEntrypoint`

The `isValidAAEntrypoint` utility is designed to verify the Account-Abstraction entrypoint before sponsoring a transaction.

## Usage

:::code-group

```tsx twoslash [code]
import { isValidAAEntrypoint } from "@coinbase/onchainkit/wallet";

const AAImplementationAddress = "0x123";
const isValid = isValidAAEntrypoint({ entrypoint: AAImplementationAddress });

if (isValid) {
  console.log("The entrypoint is valid.");
} else {
  console.log("Invalid entrypoint.");
}
```

```ts [return value]
true;
```

:::

## Returns

`boolean` - Returns `true` if the account abstraction entrypoint address is v06, otherwise `false`.

## Parameters

[`isValidAAEntrypointtOptions`](/wallet/types#isvalidaaentrypointtoptions)

base-smart-wallet.mdx -->

# `isWalletASmartCoinbaseWallet`

The `isWalletASmartCoinbaseWallet` utility is designed to verify if a given sender address is a Smart Wallet proxy with the expected implementation before sponsoring a transaction.

## Usage

:::code-group

```tsx twoslash [code]
// @noErrors: 2352 2801 2719
import { isWalletACoinbaseSmartWallet } from "@coinbase/onchainkit/wallet";
import { http } from "viem";
import { baseSepolia } from "viem/chains";
import type { UserOperation } from "permissionless";
import { type PublicClient, createPublicClient } from "viem";

export const publicClient = createPublicClient({
  chain: baseSepolia,
  transport: http(),
});

const userOperation = { sender: "0x123" } as UserOperation<"v0.6">;

if (
  isWalletACoinbaseSmartWallet({ client: publicClient, userOp: userOperation })
) {
  console.log("The sender address is a valid smart wallet proxy.");
} else {
  console.log("The sender address is not a valid smart wallet proxy.");
}
```

```ts [return value]
true;
```

:::

## Returns

[`IsWalletACoinbaseSmartWalletResponse`](/wallet/types#iswalletacoinbasesmartwalletresponse)

## Parameters

[`isWalletACoinbaseSmartWalletOptions`](/wallet/types#iswalletacoinbasesmartwalletoptions)

--

title: Wallet components & utilities types
description: Glossary of Types.

---

# Types [Glossary of Types in Wallet components & utilities.]

## `ConnectWalletReact`

```ts
type ConnectWalletReact = {
  children?: React.ReactNode; // Children can be utilized to display customized content when the wallet is connected.
  className?: string; // Optional className override for button element
  text?: string; // Optional text override for button. Note: Prefer using `ConnectWalletText` component instead as this will be deprecated in a future version.
  withWalletAggregator?: boolean; // Optional flag to enable the wallet aggregator like RainbowKit
};
```

## `IsValidAAEntrypointOptions`

```ts
export type IsValidAAEntrypointOptions = {
  entrypoint: string;
};
```

## `IsWalletACoinbaseSmartWalletOptions`

```ts
export type IsWalletACoinbaseSmartWalletOptions = {
  client: PublicClient;
  userOp: UserOperation<"v0.6">;
};
```

## `IsWalletACoinbaseSmartWalletResponse`

```ts
export type IsWalletACoinbaseSmartWalletResponse =
  | { isCoinbaseSmartWallet: true }
  | { isCoinbaseSmartWallet: false; error: string; code: string };
```

## `WalletContextType`

```ts
type WalletContextType = {
  address?: Address | null; // The Ethereum address to fetch the avatar and name for.
};
```

## `WalletReact`

```ts
type WalletReact = {
  children: React.ReactNode;
};
```

## `WalletDropdownBasenameReact`

```ts
type WalletDropdownBasenameReact = {
  className?: string; // Optional className override for the element
};
```

## `WalletDropdownReact`

```ts
type WalletDropdownReact = {
  children: React.ReactNode;
  className?: string; // Optional className override for top div element
};
```

## `WalletDropdownDisconnectReact`

```ts
export type WalletDropdownDisconnectReact = {
  className?: string; // Optional className override for the element
  text?: string; // Optional text override for the button
};
```

## `WalletDropdownFundLinkReact`

```ts
export type WalletDropdownFundLinkReact = {
  className?: string; // Optional className override for the element
  icon?: ReactNode; // Optional icon override
  openIn?: "popup" | "tab"; // Whether to open the funding flow in a tab or a popup window
  popupSize?: "sm" | "md" | "lg"; // Size of the popup window if `openIn` is set to `popup`
  rel?: string; // Specifies the relationship between the current document and the linked document
  target?: string; // Where to open the target if `openIn` is set to tab
  text?: string; // Optional text override
};
```

## `WalletDropdownLinkReact`

```ts
export type WalletDropdownLinkReact = {
  children: string;
  className?: string; // Optional className override for the element
  href: string;
  icon?: "wallet" & ReactNode;
  rel?: string;
  target?: string;
};
```

basename.mdx -->

import {
Address,
Avatar,
EthBalance,
Identity,
Name,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
ConnectWallet,
Wallet,
WalletDropdown,
WalletDropdownBasename,
WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";
import WalletComponents from "../../components/WalletComponents";

# `<WalletDropdownBasename />`

The `WalletDropdownBasename` component adds a [Basename](https://www.base.org/names) tab to the Wallet Component. This tab serves two purposes:

1. For users with a Basename: It provides a link to their Basename profile page.
2. For users without a Basename: It provides a link to a page where they can create one.

This component enhances the wallet interface by providing easy access to Basename functionality, whether for viewing an existing profile or setting up a new one.

## Usage

```tsx twoslash
import {
  Address,
  Avatar,
  Name,
  Identity,
  EthBalance,
} from "@coinbase/onchainkit/identity";
import { color } from "@coinbase/onchainkit/theme";
import {
  ConnectWallet,
  Wallet,
  WalletDropdown,
  WalletDropdownBasename, // [!code focus]
  WalletDropdownDisconnect,
} from "@coinbase/onchainkit/wallet";

export function WalletComponents() {
  return (
    <div className="flex justify-end">
      <Wallet>
        <ConnectWallet>
          <Avatar className="h-6 w-6" />
          <Name />
        </ConnectWallet>
        <WalletDropdown>
          <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
            <Avatar />
            <Name />
            <Address className={color.foregroundMuted} />
            <EthBalance />
          </Identity>
          <WalletDropdownBasename /> // [!code focus]
          <WalletDropdownDisconnect />
        </WalletDropdown>
      </Wallet>
    </div>
  );
}
```

<WalletComponents>
  <Wallet>
    <ConnectWallet text="Log In">
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownBasename />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

### Override styles

You can override component styles using `className`.

```tsx
// omitted for brevity

<WalletDropdownBasename className="hover:bg-red-500" /> // [!code focus]
```

<WalletComponents>
  <Wallet>
    <ConnectWallet text="Log In">
      <Avatar className="h-6 w-6" />
      <Name />
    </ConnectWallet>
    <WalletDropdown>
      <Identity className="px-4 pt-3 pb-2" hasCopyAddressOnClick>
        <Avatar />
        <Name />
        <Address className={color.foregroundMuted} />
        <EthBalance />
      </Identity>
      <WalletDropdownBasename className="hover:bg-red-500" />
      <WalletDropdownDisconnect />
    </WalletDropdown>
  </Wallet>
</WalletComponents>

## Props

- [`WalletDropdownBasenameReact`](/wallet/types#walletdropdownbasenamereact)

ion.mdx -->

# `buildSwapTransaction`

The `buildSwapTransaction` function is used to get an unsigned transaction for a swap between two Tokens.

Before using them, make sure to obtain a [Client API Key](https://portal.cdp.coinbase.com/projects/project-id/api-keys/client-key) from Coinbase Developer Platform.

## Usage

:::code-group

```tsx twoslash [code]
import { setOnchainKitConfig } from "@coinbase/onchainkit";
import { buildSwapTransaction } from "@coinbase/onchainkit/api";
import type { Token } from "@coinbase/onchainkit/token";

setOnchainKitConfig({ apiKey: "YOUR_API_KEY" });

const fromToken: Token = {
  name: "ETH",
  address: "",
  symbol: "ETH",
  decimals: 18,
  image:
    "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
  chainId: 8453,
};

const toToken: Token = {
  name: "USDC",
  address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
  symbol: "USDC",
  decimals: 6,
  image:
    "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
  chainId: 8453,
};

const response = await buildSwapTransaction({
  fromAddress: "0x...",
  from: fromToken,
  to: toToken,
  amount: "0.1",
  useAggregator: false,
});
```

```json [return value]
{
  "approveTransaction": {
    "chainId": 8453,
    "data": "",
    "gas": 0,
    "to": "",
    "value": 0
  },
  "fee": {
    "baseAsset": {
      "name": "USDC",
      "address": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      "currencyCode": "USDC",
      "decimals": 6,
      "imageURL": "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
      "blockchain": "eth",
      "aggregators": [Array],
      "swappable": true,
      "unverified": false,
      "chainId": 8453
    },
    "percentage": "1",
    "amount": "3517825"
  },
  "quote": {
    "from": {
      "address": "",
      "chainId": 8453,
      "decimals": 18,
      "image": "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
      "name": "ETH",
      "symbol": "ETH"
    },
    "to": {
      "address": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
      "chainId": 8453,
      "decimals": 6,
      "image": "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
      "name": "USDC",
      "symbol": "USDC"
    },
    "fromAmount": "100000000000000000",
    "toAmount": "348264739",
    "amountReference": "from",
    "priceImpact": "",
    "chainId": 8453,
    "highPriceImpact": false,
    "slippage": "3",
    "warning": {
      "type": "warning",
      "message": "This transaction has a very high likelihood of failing if submitted",
      "description": "failed with 500000000 gas: insufficient funds for gas * price + value: address 0x4ed4E862860beD51a9570b96d89aF5E1B0Efefed have 0 want 100000000000000000"
    }
  },
  "transaction": {
    "chainId": 8453,
    "data": "0x...",
    "gas": 419661,
    "to": "0xdef1c0ded9bec7f1a1670819833240f027b25eff",
    "value": 100000000000000000
  },
  "warning": {
    "type": "warning",
    "message": "This transaction has a very high likelihood of failing if submitted",
    "description": "failed with 500000000 gas: insufficient funds for gas * price + value: address 0x4ed4E862860beD51a9570b96d89aF5E1B0Efefed have 0 want 100000000000000000"
  }
}
```

:::

## Returns

[`Promise<BuildSwapTransactionResponse>`](/api/types#buildswaptransactionresponse)

## Parameters

[`BuildSwapTransactionParams`](/api/types#buildswaptransactionparams)

-->

# `getSwapQuote`

The `getSwapQuote` function is used to get a quote for a swap between two Tokens.

Before using them, make sure to obtain a [Client API Key](https://portal.cdp.coinbase.com/projects/project-id/api-keys/client-key) from Coinbase Developer Platform.

## Usage

:::code-group

```tsx twoslash [code]
import { setOnchainKitConfig } from "@coinbase/onchainkit";
import { getSwapQuote } from "@coinbase/onchainkit/api";
import type { Token } from "@coinbase/onchainkit/token";

setOnchainKitConfig({ apiKey: "YOUR_API_KEY" });

const fromToken: Token = {
  name: "ETH",
  address: "",
  symbol: "ETH",
  decimals: 18,
  image:
    "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
  chainId: 8453,
};

const toToken: Token = {
  name: "USDC",
  address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
  symbol: "USDC",
  decimals: 6,
  image:
    "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
  chainId: 8453,
};

const quote = await getSwapQuote({
  from: fromToken,
  to: toToken,
  amount: "0.001",
  useAggregator: false,
});
```

```json [return value]
{
  "amountReference": "from",
  "chainId": 8453,
  "from": {
    "address": "",
    "chainId": 8453,
    "decimals": 18,
    "image": "https://wallet-api-production.s3.amazonaws.com/uploads/tokens/eth_288.png",
    "name": "ETH",
    "symbol": "ETH"
  },
  "to": {
    "address": "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
    "chainId": 8453,
    "decimals": 6,
    "image": "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/…-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
    "name": "USDC",
    "symbol": "USDC"
  },
  "fromAmount": "1000000000000000",
  "fromAmountUSD": "2.6519265340000002",
  "toAmount": "2650405",
  "toAmountUSD": "2.64980125",
  "amountReference": "from",
  "priceImpact": "0",
  "chainId": 8453,
  "highPriceImpact": false,
  "slippage": "3"
}
```

:::

## Returns

[`Promise<GetSwapQuoteResponse>`](/api/types#getswapquoteresponse)

## Parameters

[`GetSwapQuoteParams`](/api/types#getswapquoteparams)

title: API types
description: Glossary of Types.

---

# Types [Glossary of Types in APIs.]

## `APIError`

```ts
type APIError = {
  code: string; // The Error code
  error: string; // The Error long message
  message: string; // The Error short message
};
```

## `BuildPayTransactionParams`

```ts
type BuildPayTransactionParams = {
  address: Address; // The address of the wallet paying
  chainId: number; // The Chain ID of the payment Network (only Base is supported)
  chargeId: string; // The ID of the Commerce Charge to be paid
};
```

## `BuildPayTransactionResponse`

```ts
type BuildPayTransactionResponse = PayTransaction | APIError;
```

## `BuildSwapTransaction`

```ts
type BuildSwapTransaction = {
  approveTransaction?: Transaction; // ERC20 approve transaction which allows token holders to authorize spending
  fee: Fee; // The fee for the swap
  quote: SwapQuote; // The quote for the swap
  transaction: Transaction; // The object developers should pass into Wagmi's signTransaction
  warning?: QuoteWarning; // The warning associated with the swap
};
```

## `BuildSwapTransactionParams`

```ts
type BuildSwapTransactionParams = GetSwapQuoteParams & {
  fromAddress: Address; // The address of the user
};
```

## `BuildSwapTransactionResponse`

```ts
type BuildSwapTransactionResponse = BuildSwapTransaction | APIError;
```

## `GetSwapQuoteParams`

```ts
type GetSwapQuoteParams = {
  amount: string; // The amount to be swapped
  amountReference?: string; // The reference amount for the swap
  from: Token; // The source token for the swap
  isAmountInDecimals?: boolean; // Whether the amount is in decimals
  maxSlippage?: string; // The slippage of the swap
  to: Token; // The destination token for the swap
  useAggregator: boolean; // Whether to use a DEX aggregator
};
```

## `GetSwapQuoteResponse`

```ts
type GetSwapQuoteResponse = SwapQuote | APIError;
```

## `GetTokensOptions`

```ts
type GetTokensOptions = {
  limit?: string; // The maximum number of tokens to return (default: 50)
  page?: string; // The page number to return (default: 1)
  search?: string; // A string to search for in the token name, symbol or address
};
```

## `GetTokensResponse`

```ts
type GetTokensResponse = Token[] | APIError;
```

# `getTokens`

The `getTokens` function retrieves a list of tokens on Base by searching for the name, symbol, or address of a token.

Before using them, make sure to obtain a [Client API Key](https://portal.cdp.coinbase.com/projects/project-id/api-keys/client-key) from Coinbase Developer Platform.

## Usage

Search by symbol

:::code-group

```tsx twoslash [code]
import { setOnchainKitConfig } from "@coinbase/onchainkit";
import { getTokens } from "@coinbase/onchainkit/api"; // [!code focus]

setOnchainKitConfig({ apiKey: "YOUR_API_KEY" });

const tokens = await getTokens({ limit: "1", search: "degen" }); // [!code focus]
```

```ts [return value]
[
  {
    address: "0x4ed4e862860bed51a9570b96d89af5e1b0efefed",
    chainId: 8453,
    decimals: 18,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/3b/bf/3bbf118b5e6dc2f9e7fc607a6e7526647b4ba8f0bea87125f971446d57b296d2-MDNmNjY0MmEtNGFiZi00N2I0LWIwMTItMDUyMzg2ZDZhMWNm",
    name: "DEGEN",
    symbol: "DEGEN",
  },
];
```

:::

Search by name

:::code-group

```tsx twoslash [code]
import { setOnchainKitConfig } from "@coinbase/onchainkit";
import { getTokens } from "@coinbase/onchainkit/api"; // [!code focus]

setOnchainKitConfig({ apiKey: "YOUR_API_KEY" });

const tokens = await getTokens({ limit: "1", search: "Wrapped Ether" }); // [!code focus]
```

```ts [return value]
[
  {
    address: "0x4200000000000000000000000000000000000006",
    chainId: 8453,
    decimals: 18,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/47/bc/47bc3593c2dec7c846b66b7ba5f6fa6bd69ec34f8ebb931f2a43072e5aaac7a8-YmUwNmRjZDUtMjczYy00NDFiLWJhZDUtMzgwNjFmYWM0Njkx",
    name: "Wrapped Ether",
    symbol: "WETH",
  },
];
```

:::

Search by address

:::code-group

```tsx twoslash [code]
import { setOnchainKitConfig } from "@coinbase/onchainkit";
import { getTokens } from "@coinbase/onchainkit/api"; // [!code focus]

setOnchainKitConfig({ apiKey: "YOUR_API_KEY" });

const tokens = await getTokens({
  limit: "1",
  search: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
}); // [!code focus]
```

```ts [return value]
[
  {
    address: "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913",
    chainId: 8453,
    decimals: 6,
    image:
      "https://d3r81g40ycuhqg.cloudfront.net/wallet/wais/44/2b/442b80bd16af0c0d9b22e03a16753823fe826e5bfd457292b55fa0ba8c1ba213-ZWUzYjJmZGUtMDYxNy00NDcyLTg0NjQtMWI4OGEwYjBiODE2",
    name: "USDC",
    symbol: "USDC",
  },
];
```

:::

## Returns

[`Promise<GetTokensResponse>`](/api/types#gettokensresponse)

## Parameters

[`GetTokensOptions`](/api/types#gettokensoptions)

sage.mdx -->

# `getXmtpFrameMessage`

Frames can receive interactions from apps outside of Farcaster, such as from XMTP conversations.
When receiving these interactions you can expect a slightly different response format,
since fields like `fid` or `castId` are not available.

You can also use `getXmtpFrameMessage` to access useful information such as:

- buttonIndex: number
- verifiedWalletAddress: string
- opaqueConversationIdentifier: string

Note that if the `message` is not valid, it will be undefined.

```ts twoslash
// @noErrors: 2307 2339 - Cannot find module 'next/server', Property 'verifiedWalletAddress' does not exist on type
import {
  isXmtpFrameRequest,
  getXmtpFrameMessage,
} from "@coinbase/onchainkit/xmtp"; // [!code focus]
import { NextResponse } from "next/server";
import type { FrameRequest } from "@coinbase/onchainkit/frame";

async function getResponse(req: any): Promise<NextResponse> {
  const body: FrameRequest = await req.json();
  if (isXmtpFrameRequest(body)) {
    const { isValid, message } = await getXmtpFrameMessage(body); // [!code focus]
    // ... do something with the message if isValid is true
    if (isValid) {
      const { verifiedWalletAddress } = message;
      // ... do something with the verifiedWalletAddress
    }
  } else {
    // ...
  }
}
```

## Returns

[`Promise<XmtpFrameValidationResponse>`](/xmtp/types#xmtpframevalidationresponse)

## Parameters

[`Promise<XmtpFramesRequest>`](/xmtp/types#xmtpframesrequest)

est.mdx -->

# `isXmtpFrameRequest`

```ts twoslash
// @noErrors: 2307 - Cannot find module 'next/server'
import { FrameRequest } from "@coinbase/onchainkit/frame";
import { isXmtpFrameRequest } from "@coinbase/onchainkit/xmtp"; // [!code focus]
import { NextResponse } from "next/server";

async function getResponse(req: any): Promise<NextResponse> {
  const body: FrameRequest = await req.json();
  if (isXmtpFrameRequest(body)) {
    // ...
  }
}
```

## Returns

- **Type:** `boolean`

## Parameters

[`XmtpFramesRequest`](/xmtp/types#xmtpframesrequest)

->

---

title: Introduction to XMTP utilities · OnchainKit
description: Introduction to XMTP utilities

---

# Introduction to XMTP utilities

OnchainKit has a collection of utilities that allows you to build Frames with the XMTP protocol.

## Metadata

To build a Frame with XMTP, you must first add XMTP metadata. This is done using the `getFrameMetadata` function.

```ts
const frameMetadata = getFrameMetadata({
  /**
   * Frame metadata like Image, Buttons, Input, etc.
   */
  isOpenFrame: true,
  accepts: { xmtp: "vNext" },
});

export const metadata: Metadata = {
  /**
   * ...other metadata
   */
  other: {
    ...frameMetadata,
  },
};
```

- `isOpenFrame`: A boolean that indicates whether the Frame is open or not.
- `accepts`: An object that indicates the versions of the Frame that the Frame supports.

## Handling XMTP Frames

When a user interacts with a Frame inside an XMTP client application, you will need to handle the payload slightly differently from an interaction coming from Farcaster. The primary identifier for a user on Farcaster is the `fid`, while in XMTP it is the `verifiedWalletAddress`.

In order to get the `verifiedWalletAddress` you must install `@xmtp/frames-validator` in your Frame, alongside Onchainkit.

:::code-group

```bash [npm]
npm install @coinbase/onchainkit @xmtp/frames-validator
```

```bash [yarn]
yarn add @coinbase/onchainkit @xmtp/frames-validator
```

```bash [pnpm]
pnpm add @coinbase/onchainkit @xmtp/frames-validator
```

```bash [bun]
bun add @coinbase/onchainkit @xmtp/frames-validator
```

:::

To assist you in handling interactions from XMTP, and extracting the `verifiedWalletAddress` from a POST payload, here is the XMTP utilities which includes:

- [XMTP](/xmtp/introduction)
  - Utilities:
    - [`getXmtpFrameMessage`](/xmtp/get-xmtp-frame-message)
    - [`isXmtpFrameRequest`](/xmtp/is-xmtp-frame-request)

title: Xmtp Types
description: Glossary of Types in Xmtp.

---

# Types [Glossary of Types in Xmtp.]

## `XmtpFramesRequest`

```ts
export type UntrustedData = {
  url: string;
  timestamp: number;
  buttonIndex: number;
  inputText?: string;
  opaqueConversationIdentifier: string;
  walletAddress: string;
};

// The Frame Signature Packet body
export type XmtpFramesRequest = {
  clientProtocol: `xmtp@${string}`;
  untrustedData: UntrustedData;
  trustedData: {
    messageBytes: string;
  };
};
```

## `XmtpFrameValidationResponse`

```ts
type XmtpFrameValidationResponse =
  | { isValid: true; message: XmtpFrameValidationData }
  | { isValid: false; message: undefined };
```

>

---

title: <FundButton /> · OnchainKit
description: The `<FundButton />` components provides a way for users to onramp from fiat to crypto from within your app.

---

import { Avatar, Name } from "@coinbase/onchainkit/identity";
// import { FundButton } from '../../../../src/fund';
import { FundButton, getOnrampBuyUrl } from "@coinbase/onchainkit/fund";
import { Wallet, ConnectWallet } from "@coinbase/onchainkit/wallet";
import FundWrapper from "../../components/FundWrapper";

# `<FundButton />`

The `<FundButton />` component provides a way for users to fund their wallet without leaving your app. It automatically
detects the user's wallet type (EOA vs Smart Wallet) and directs them to the appropriate funding URL.

If your user connects a Coinbase Smart Wallet, it provides an easy way to access the Coinbase Smart Wallet
[Fund](https://keys.coinbase.com/fund) flow. Users will be able to buy and receive crypto, or use their Coinbase
balances onchain with [Magic Spend](https://www.smartwallet.dev/guides/magic-spend).

If your user connects any other EOA wallet, it provides an easy way to access [Coinbase Onramp](https://docs.cdp.coinbase.com/onramp/docs/welcome/)
where your users will also be able to buy crypto using a fiat payment method, or transfer existing crypto from their
Coinbase account.

Before using it, ensure you've completed all [Getting Started steps](/getting-started).

## Walkthrough

::::steps

### Get your Project ID

1. Get your Project ID from the [Coinbase Developer Platform Dashboard](https://portal.cdp.coinbase.com/).

<img alt="OnchainKit copy Project Id" src="../../assets/copy-project-id.png" />

2. Add your Project ID to your `.env` file.

```tsx twoslash [.env]
// @noErrors
NEXT_PUBLIC_ONCHAINKIT_API_KEY = YOUR_PUBLIC_API_KEY;
NEXT_PUBLIC_CDP_PROJECT_ID = YOUR_CDP_PROJECT_ID; // [!code ++]
```

### Add Project ID to OnchainKitProvider

```tsx twoslash
// @noErrors
<OnchainKitProvider
  apiKey={process.env.NEXT_PUBLIC_ONCHAINKIT_API_KEY}
  projectId={process.env.NEXT_PUBLIC_CDP_PROJECT_ID} // [!code ++]
  chain={base}
>
  {props.children}
</OnchainKitProvider>
```

### Drop in the `<FundButton />` component

```tsx
import { FundButton } from "@coinbase/onchainkit/fund";

<FundButton />;
```

<App>
  <FundWrapper>
    {({ address }) => {
      if (address) {
        return <FundButton />;
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </FundWrapper>
</App>

::::

:::tip[Troubleshooting]
If you see a "something went wrong" error message when navigating to pay.coinbase.com, make sure you have "enforce
secure initialization" disabled on the [Onramp config page in Coinbase Developer Platform Dashboard](https://portal.cdp.coinbase.com/products/onramp).

<img
  alt="OnchainKit require secure init"
  src="../../assets/onramp-secure-init.png"
/>
:::

## Customizing the funding experience

You can customize the Coinbase Onramp experience by bringing your own Onramp URL and passing it to the `<FundButton />`
component. We provide the [`getOnrampBuyUrl`](/fund/get-onramp-buy-url) utility to help you generate a Coinbase Onramp
URL tailored to your use case.

```tsx
import { FundButton, getOnrampBuyUrl } from "@coinbase/onchainkit/fund";
import { useAccount } from "wagmi";

const projectId = "YOUR_CDP_PROJECT_ID";
const { address } = useAccount();

const onrampBuyUrl = getOnrampBuyUrl({
  projectId,
  addresses: { address: ["base"] },
  assets: ["USDC"],
  presetFiatAmount: 20,
  fiatCurrency: "USD",
});

<FundButton fundingUrl={onrampBuyUrl} />;
```

<App>
  <FundWrapper>
    {({ address, projectId }) => {
      if (address && projectId) {
        const onrampBuyUrl = getOnrampBuyUrl({
          projectId,
          addresses: { [address]: ["base"] },
          assets: ["USDC"],
          presetFiatAmount: 20,
          fiatCurrency: "USD",
        });
        return <FundButton fundingUrl={onrampBuyUrl} />;
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </FundWrapper>
</App>

You can choose to have the funding URL open in a popup or a new tab using the `openIn` prop.

```tsx
<FundButton openIn={"tab"} />
```

<App>
  <FundWrapper>
    {({ address }) => {
      if (address) {
        return <FundButton openIn={"tab"} />;
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </FundWrapper>
</App>

## Customizing the fund button

You can override the text on the fund button using the `text` prop, and hide the icon with the `hideIcon` prop.

```tsx
<FundButton text={"Onramp"} hideIcon={true} />
```

<App>
  <FundWrapper>
    {({ address }) => {
      if (address) {
        return <FundButton text={"Onramp"} hideIcon={true} />;
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </FundWrapper>
</App>

You can hide the text with the `hideText` prop.

```tsx
<FundButton hideText={true} />
```

<App>
  <FundWrapper>
    {({ address }) => {
      if (address) {
        return (
          <>
            <FundButton hideText={true} />
          </>
        );
      }
      return (
        <>
          <Wallet>
            <ConnectWallet>
              <Avatar className="h-6 w-6" />
              <Name />
            </ConnectWallet>
          </Wallet>
        </>
      );
    }}
  </FundWrapper>
</App>

See [`FundButtonReact`](/fund/types#fundbuttonreact) for the full list of customization options.

## Props

- [`FundButtonReact`](/fund/types#fundbuttonreact)

title: Fund components & utilities types
description: Glossary of Types.

---

# Types [Glossary of Types in Fund components & utilities.]

## `FundButtonReact`

```ts
type FundButtonReact = {
  className?: string; // An optional CSS class name for styling the button component
  disabled?: boolean; // A optional prop to disable the fund button
  text?: string; // An optional text to be displayed in the button component
  hideText?: boolean; // An optional prop to hide the text in the button component
  hideIcon?: boolean; // An optional prop to hide the icon in the button component
  fundingUrl?: string; // An optional prop to provide a custom funding URL
  openIn?: "popup" | "tab"; // Whether to open the funding flow in a tab or a popup window
  /**
   * Note: popupSize will be ignored when using a Coinbase Onramp URL
   * (i.e. https://pay.coinbase.com/*) as it requires a fixed popup size.
   */
  popupSize?: "sm" | "md" | "lg"; // Size of the popup window if `openIn` is set to `popup`
  rel?: string; // Specifies the relationship between the current document and the linked document
  target?: string; // Where to open the target if `openIn` is set to tab
};
```

## `GetOnrampUrlWithProjectIdParams`

Props used to get an Onramp buy URL by directly providing a CDP project ID.

See https://docs.cdp.coinbase.com/onramp/docs/api-initializing#generating-the-coinbase-onramp-buysell-url

```ts
type GetOnrampUrlWithProjectIdParams = {
  /**
   * The Project ID of your CDP project created at {@link https://portal.cdp.coinbase.com/}
   * This must be provided if you don't provide a sessionToken.
   */
  projectId: string;
  sessionToken?: never; // You cannot provide sessionToken when using projectId
  /**
   * The addresses that the customer's funds should be delivered to.
   *
   * Each entry in the record represents a wallet address and the networks it is valid for. There should only be a
   * single address for each network your app supports. Users will be able to buy/send any asset supported by any of
   * the networks you specify. See the assets param if you want to restrict the avaialable assets.
   *
   * Some common examples:
   *
   * Support all assets that are available for sending on the base network, only on the base network:
   *
   * `{ "0x1": ["base"] }`
   */
  addresses: Record<string, string[]>;
  /**
   * This optional parameter will restrict the assets available for the user to buy/send. It acts as a filter on the
   * networks specified in the {addresses} param.
   *
   * Some common examples:
   *
   * Support only USDC on either the base network or the ethereum network:
   *
   * `addresses: { "0x1": ["base", "ethereum"] }, assets: ["USDC"]`
   *
   * The values in this list can either be asset symbols like BTC, ETH, or asset UUIDs that you can get from the Buy
   * Options API {@link https://docs.cdp.coinbase.com/onramp/docs/api-configurations/#buy-options}.
   */
  assets?: string[];
} & GetOnrampBuyUrlOptionalProps;
```

## `GetOnrampUrlWithSessionTokenParams`

Props used to get an Onramp buy URL using a session token created using the Onramp session token API.

See https://docs.cdp.coinbase.com/onramp/docs/api-initializing#getting-an-coinbase-onramp-buysell-session-token

```ts
type GetOnrampUrlWithSessionTokenParams = {
  /**
   * A session token create using the Onramp session token API. The token will
   * be linked to the project ID, addresses, and assets params provided in the
   */
  sessionToken: string;
  projectId?: never; // You cannot provide projectId when using sessionToken
  addresses?: never; // You cannot provide addresses when using sessionToken
  assets?: never; // You cannot provide assets when using sessionToken
} & GetOnrampBuyUrlOptionalProps;
```

## `GetOnrampBuyUrlOptionalProps`

The optional properties that can be used to create an Onramp buy URL.

```ts
type GetOnrampBuyUrlOptionalProps = {
  /**
   * If specified, this asset will be automatically selected for the user in
   * the Onramp UI. Should be a valid asset symbol e.g. BTC, ETH, USDC.
   */
  defaultAsset?: string;
  /**
   * If specified, this network will be automatically selected for the user in
   * the Onramp UI. Should be a valid network name in lower case e.g. ethereum,
   * base.
   */
  defaultNetwork?: string;
  /**
   * A unique identifier that will be associated with any transactions created
   * by the user during their Onramp session. You can use this with the
   * Transaction Status API to check the status of the user's transaction.
   * See https://docs.cdp.coinbase.com/onramp/docs/api-reporting#buy-transaction-status
   */
  partnerUserId?: string;
  /**
   * This amount will be used to pre-fill the amount of crypto the user is
   * buying or sending. The user can choose to change this amount in the UI.
   * Only one of presetCryptoAmount or presetFiatAmount should be provided.
   */
  presetCryptoAmount?: number;
  /**
   * This amount will be used to pre-fill the fiat value of the crypto the user
   * is buying or sending. The user can choose to change this amount in the UI.
   * Only one of presetCryptoAmount or presetFiatAmount should be provided.
   */
  presetFiatAmount?: number;
  /**
   * The currency code of the fiat amount provided in the presetFiatAmount
   * param e.g. USD, CAD, EUR.
   */
  fiatCurrency?: string;
  /**
   * A URL that the user will be automatically redirected to after a successful
   * buy/send. The domain must match a domain on the domain allowlist in
   * Coinbase Developer Platform (https://portal.cdp.coinbase.com/products/onramp).
   */
  redirectUrl?: string;
};
```

.mdx -->

# `getOnrampBuyUrl`

The `getOnrampBuyUrl` utility is a helper method to generate a Coinbase Onramp URL. It helps you customize the funding
experience for your users. For example:

- Selecting which assets should be available to buy/send
- Selecting which networks crypto should be received on
- Setting a default buy/send amount
- Setting a redirect URL to return your users to your app after they complete the fund flow

See the
[Coinbase Onramp docs](https://docs.cdp.coinbase.com/onramp/docs/generating-url) for detailed descriptions of all the
available parameters.

## Usage

:::code-group

```tsx twoslash [code]
import { getOnrampBuyUrl } from "@coinbase/onchainkit/fund";

const projectId = "YOUR_CDP_PROJECT_ID";
const onrampBuyUrl = getOnrampBuyUrl({
  projectId,
  addresses: { "0x1": ["base"] },
  assets: ["USDC"],
  presetFiatAmount: 20,
  fiatCurrency: "USD",
  redirectUrl: "https://yourapp.com/onramp-return?param=foo",
});
```

```ts [return value]
"https://pay.coinbase.com/buy?addresses=%7B%220x1%22%3A%5B%22base%22%5D%7D&appId=project-id&assets=%5B%22USDC%22%5D&fiatCurrency=USD&presetFiatAmount=20&redirectUrl=https%3A%2F%2Fyourapp.com%2Fonramp-return%3Fparam%3Dfoo";
```

:::

## Returns

`string` - Returns a full Coinbase Onramp URL that you can redirect your users to, or open in a popup.

## Parameters

[`GetOnrampUrlWithProjectIdParams`](/fund/types#getonrampurlwithsessiontokenparams) | [`GetOnrampUrlWithSessionTokenParams`](/fund/types#getonrampurlwithsessiontokenparams)
