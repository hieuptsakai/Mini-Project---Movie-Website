<template lang="pug">
v-card
    .upload-pic.d-flex.justify-space-around.align-center 
        .ma-4 
            v-img(width="80" :aspect-ratio="1" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/OOjs_UI_icon_upload.svg/120px-OOjs_UI_icon_upload.svg.png")
    .pic-load.d-flex.justify-space-around
        v-img( :aspect-ratio="1" src="https://www.truyentranhlh.net/storage/images/raw/b8298c80-82d5-4418-b45a-63c1c4ae20a2.jpg").up-pic
    .comfirm-btn 
        .d-flex.justify-space-around.align-center.flex-column.flex-sm-row.fill-height
            v-btn(flat color="error") Cancel 
            v-btn(flat color="secondary") Confirm   
</template>
    
<script>
    
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