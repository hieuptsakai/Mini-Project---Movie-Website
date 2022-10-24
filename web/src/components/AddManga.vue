<template lang="pug">
v-card
    .upload-pic.d-flex.justify-space-around.align-center 
        .ma-4 
            v-img(width="80" :aspect-ratio="1" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/OOjs_UI_icon_upload.svg/120px-OOjs_UI_icon_upload.svg.png")
    .pic-load.d-flex.justify-space-around
        v-img( :aspect-ratio="1" src="https://www.truyentranhlh.net/storage/images/raw/b8298c80-82d5-4418-b45a-63c1c4ae20a2.jpg").up-pic
    .up-manga-detail 
        v-form(ref="form" v-model="valid" lazy-validation)
            span Manga name:
            v-text-field(v-model="name" :counter="40" :rules="nameRules" placeholder="Manga Name" required)
            span Genre:
            v-select(v-model="select" :items="genres" :rules="[v => !!v || 'Genre is required']" placeholder="Genre" required)
            span Author:
            v-text-field(v-model="author" :rules="authorRules" placeholder="Author" required)
            span Summary:
            v-text-field(v-model="summary" :rules="summaryRules" placeholder="Summary" required)
    .comfirm-btn 
        .d-flex.justify-space-around.align-center.flex-column.flex-sm-row.fill-height
            v-btn(flat color="error") Cancel 
            v-btn(flat color="secondary") Confirm

</template>

<script>
export default {
    data: () => ({
        valid: true,
        name: '',
        nameRules: [
            v => !!v || 'Manga name is required',
        ],
        select: null,
        genres: [
            'Genre 1',
            'Genre 2',
            'Genre 3',
        ],
        author: '',
        authorRules: [
            v => !!v || 'Author name is required',
        ],
        summary: '',
        summaryRules: [
            v => !!v || 'Summary is required',
        ]
    })
}

</script>

<style lang="scss" scoped>
.upload-pic{
    border-radius: 0.5rem;
    border: 1px dashed black;
    margin: 2rem;
    padding: 3rem;
}
.pic-load{
    padding: 0 1rem 1rem 2rem;
    width: 170px;
}
.up-pic{
    height: 150px;
}
.up-manga-detail {
    padding: 1rem;
}
.comfirm-btn {
    padding-bottom: 2rem;
}
</style>