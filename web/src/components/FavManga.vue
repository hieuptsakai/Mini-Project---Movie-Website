<template lang="pug">
v-card
    v-row
        v-col(cols="7").fav-pic
            v-img(width="160" :aspect-ratio="1" src="https://www.truyentranhlh.net/storage/images/raw/b8e46094-b25a-42cb-ac41-b5363ca32112.jpg").bg-white
        v-col(cols="5").fav-name
            h5 {{name}}
</template>

<script setup>
defineProps({
    name: {
        type: String,
        required: true
    },
    pic: {
        type: String,
        required: true
    }
})
</script>

<style lang="scss" scoped>
.v-card{
    padding: 0.5rem;
    margin: 8px 0;
    .fav-pic{
        padding-right: 0px;
    }
    .fav-name{
        padding-left: 0px;
    }
}
</style>