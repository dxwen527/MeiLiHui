$(function () {
    var swiper = new Swiper('.swiper-container', {
        // navigation: {
        //   // nextEl: '.swiper-button-next',
        //   // prevEl: '.swiper-button-prev',
        //
        // },
        // spaceBetween: 30,

        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            autoplay: 3000,
            slidesPerView: 1,
            loop: true,
        },
    });
})