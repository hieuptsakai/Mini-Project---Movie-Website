<template lang="pug">
v-footer(fluid).bg-pink-lighten-3.text-center.d-flex.flex-column
    div
        v-btn(v-for="icon in icon" :key="icon" :icon="icon" variant="text").mx-4
        v-diviver 
        div {{ new Date().getFullYear() }} — <strong>Sakai</strong>
</template>

<script>
export default {
    data: () => ({
        icons: [
            'mdi-facebook',
            'mdi-twitter',
            'mdi-linkedin',
            'mdi-instagram',
        ],
    }),
}
</script>

<style lang="scss">
</style>