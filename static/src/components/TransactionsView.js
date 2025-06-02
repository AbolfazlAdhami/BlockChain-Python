export default {
  props: ["txLoading", "outgoingTx"],
  template: `
      <form @submit.prevent="$emit('send-tx')" class="space-y-4 mb-6">
        <div>
          <label for="recipient" class="block text-sm font-medium text-gray-700">Recipient Key</label>
          <input v-model="outgoingTx.recipient" type="text" 
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500" 
            id="recipient" placeholder="Enter key" />
        </div>
        <div>
          <label for="amount" class="block text-sm font-medium text-gray-700">Amount of Coins</label>
          <input v-model.number="outgoingTx.amount" type="number" step="0.001" 
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500" 
            id="amount" />
          <p class="mt-2 text-sm text-gray-500">Fractions are possible (e.g. 5.67)</p>
        </div>
        <div v-if="txLoading" class="lds-ring">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
        <button :disabled="txLoading || outgoingTx.recipient.trim() === '' || outgoingTx.amount <= 0" 
          type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded 
          disabled:opacity-50 disabled:cursor-not-allowed">Send</button>
      </form>
    `,
};
