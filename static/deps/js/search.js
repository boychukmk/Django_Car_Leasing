document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.querySelector('.search-icon');
    const searchFormWrapper = document.querySelector('.search-form-wrapper');

    searchIcon.addEventListener('click', function () {
        searchFormWrapper.classList.toggle('active');
    });

    document.addEventListener('click', function (event) {
        if (!searchFormWrapper.contains(event.target) && !searchIcon.contains(event.target)) {
            searchFormWrapper.classList.remove('active');
        }
    });
});
