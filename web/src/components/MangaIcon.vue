<template lang="pug">
v-card.manga-icon
    v-img(width="160" :aspect-ratio="1" src="https://www.truyentranhlh.net/storage/images/raw/b8e46094-b25a-42cb-ac41-b5363ca32112.jpg").bg-white
    h4.manga-name {{name}}
</template>

<script setup>
defineProps({
    name: {
        type: String,
        required: true
    }
})
</script>

<style>
.manga-icon {
    max-width: 16;
}

.manga-name{
    text-align: center;
    padding: 0 1rem;
    height: 75px;
}
</style>