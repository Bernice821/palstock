<template>
  <div class="about">
    <Market/>
  </div>
</template>

<script>
// @ is an alias to /src
import Market from '@/components/MarketPage.vue'

export default {
  name: 'HomeView',
  components: {
    Market
  }
}
</script>
