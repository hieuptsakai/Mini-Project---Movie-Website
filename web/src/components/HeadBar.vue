<template lang="pug">
v-app-bar(color="#F48FB1" dense dark)
    v-img(src="https://otani.vn/images/logo.svg")
    v-spacer 
    v-text-field(label="Search" placeholder="Name the Manga..." filled rounded dense)
    v-btn(icon) 
        v-icon mdi-magnify 

</template>

<script>
export default {
    data: () => ({
    })
}
</script>

<style lang="scss" scoped>
.v-input {
    height: 58px;
    margin-right: 5px;
}


</style>