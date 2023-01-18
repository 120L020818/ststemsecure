<template>
  <router-view> </router-view>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  mounted() {
    this.$router.replace({name:'test'})
  }
}
</script>

<style scoped>

</style>
