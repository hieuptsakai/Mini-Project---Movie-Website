<template lang="pug" >
v-app-bar(color="white" dense).admin_title
    span.text-h6 Admin_Name
    v-spacer 
    v-dialog(v-model="dialog1" max-width="50%")
        template(v-slot:activator="{props}")
            v-btn(v-bind="props" value="addmanga").add_btn Add Manga
        AddManga
v-table(density="compact")
    thead  
        tr
            th.text-left ID
            th.text-left Name
            th.text-left Summary 
            th.text-center Action 
    tbody
        tr(v-for="item in mangalist" :key="item.name")
            td.bg-orange-lighten-3 {{item.id}}
            td.bg-orange-lighten-3 {{item.name}}
            td.bg-orange-lighten-3 {{item.summary}}
            v-table 
                tbody
                    tr.add_btn
                        v-dialog(v-model="dialog2" max-width="50%")
                            template(v-slot:activator="{props}")
                                v-btn(v-bind="props" value="addchapter").bg-green-lighten-2.text-left Add Manga +
                            AddChapter
                    tr.del_btn
                        v-btn(v-bind="props" value="addchapter" width="100%").bg-red-lighten-2.text-left Del Manga -
                        
                        
</template>

<script>
import AddManga from './AddManga.vue';
import { mergeProps } from 'vue'
import AddChapter from './AddChapter.vue'

export default {
data() {
    return {
        mangalist: [
            {
                id: 1,
                name: "TENSEI SHITARA KEN DESHITA",
                summary: "Khi nhận ra thì ... tôi đang ở 1 thế giới khác. Tôi đã trở thành 1 thanh kiếm, wtf? Chuyện éo gì thế này? Chỗ tôi tỉnh dậy sao lại toàn quái vật thế này ... Tôi liền bay đi kiếm ngay 1 cộng sự cho mình (Chỉ gái thui nhá). 1 viên ma pháp thạch? Tôi có dc những kĩ năng mà mình hấp thụ? Vui vkl hahaha , mau đưa ta viên ma pháp thạch! À đùa đấy, nhưng ta vẫn sẽ lấy nó ... Đây là cách mà tôi đã chuyển sinh thành 1 thanh kiếm ở thế giới khác đó, câu chuyện của 1 tên Otaku",
                action1: "Add Manga +",
                action2: "Delete Manga -",
            },
        ],
        toggle_none: null,
        toggle_one: 0,
        toggle_exclusive: 2,
        toggle_multiple: [0, 1, 2],
        dialog1: false,
        dialog2: false,
    };
},
components: { AddManga, AddChapter }
}
</script>

<styles lang="scss">
.admin_title{
    padding-left: 1rem;
    width: 80%;
}

.add_btn{
    background-color: #4BDA13;
}
</styles>