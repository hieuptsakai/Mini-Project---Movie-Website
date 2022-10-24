<template lang="pug">
.manga-detail 
    v-card
        v-row
            v-col(cols="3")
                v-img(height="100%" :aspect-ratio="1" src="https://www.truyentranhlh.net/storage/images/raw/b8e46094-b25a-42cb-ac41-b5363ca32112.jpg").bg-white.manga.pic
            v-col(cols="9")
                    v-card-title Kowloon Generic Romance 
                    v-divider
                    v-card-title Summary 
                    span.summary-text Khi nhận ra thì ... tôi đang ở 1 thế giới khác. Tôi đã trở thành 1 thanh kiếm, wtf? Chuyện éo gì thế này? Chỗ tôi tỉnh dậy sao lại toàn quái vật thế này ... Tôi liền bay đi kiếm ngay 1 cộng sự cho mình (Chỉ gái thui nhá). 1 viên ma pháp thạch? Tôi có dc những kĩ năng mà mình hấp thụ? Vui vkl hahaha , mau đưa ta viên ma pháp thạch! À đùa đấy, nhưng ta vẫn sẽ lấy nó ... Đây là cách mà tôi đã chuyển sinh thành 1 thanh kiếm ở thế giới khác đó, câu chuyện của 1 tên Otaku
                    v-card-title Author: Tanaka Yuu
                    v-card-title Genre: Action, Adventure, Comedy, Fantasy, Shounen
                    v-divider
                    v-card-title Chapter 
                    a(href="#").select-chapter
                        span.summary-text Chapter 1
                    a(href="#").select-chapter
                        span.summary-text Chapter 2 
                    a(href="#").select-chapter
                        span.summary-text Chapter 3 
                    a(href="#").select-chapter
                        span.summary-text Chapter 4 
                    a(href="#").select-chapter
                        span.summary-text Chapter 5 
                    a(href="#").select-chapter
                        span.summary-text Chapter 6
                    a(href="#").select-chapter
                        span.summary-text Chapter 7 
                    a(href="#").select-chapter
                        span.summary-text Chapter 8 
                    a(href="#").select-chapter
                        span.summary-text Chapter 9 
                    a(href="#").select-chapter
                        span.summary-text Chapter 10


    </template>

<script>

</script>

<style lang="scss"> 
.manga-detail{
    padding: 0;
    margin: 0px;
}
.v-img__img .manga-pic{
    padding: 1rem;
}
.summary-text{
    padding: 1rem;
}
.select-chapter{
    padding-top: 0.5rem;
}
</style>