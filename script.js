document.addEventListener('DOMContentLoaded', function () {
    var fadeContainer = document.getElementById('fadeContainer');
    
    window.addEventListener('scroll', function () {
        var scrollTop = window.scrollY;

        // Calculate the opacity based on the scroll position
        var opacity = Math.min(1, scrollTop / 200);

        // Apply the background color with the calculated opacity
        fadeContainer.style.backgroundColor = 'rgba(14, 14, 14, ' + opacity + ')';
    });
});