export default {
  props: ["walletLoading", "funds"],
  template: `
      <div class="flex justify-between items-center mb-6">
        <div>
          <div v-if="!walletLoading" class="space-x-2">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" 
              @click="$emit('create-wallet')">Create new Wallet</button>
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" 
              @click="$emit('load-wallet')">Load Wallet</button>
          </div>
          <div v-if="walletLoading" class="lds-ring">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div>
        <div>
          <h2 class="text-2xl font-semibold">Funds: {{ funds.toFixed(2) }}</h2>
        </div>
      </div>
    `,
};
