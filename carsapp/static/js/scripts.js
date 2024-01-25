// misc functions
function scrollTo(hash) {
  location.hash = '#' + hash;
}
console.log('scripts.js loaded');
const tooltips = document.querySelectorAll('.tooltip');
const favorites = document.querySelectorAll('.favorite');

favorites.forEach(function (favorite) {
  favorite.addEventListener('mouseover', function () {
    console.log('favorite');
    tooltips.forEach(function (tooltip) {
      tooltip.classList.add('show');
    });
  });

  favorite.addEventListener('mouseout', function () {
    tooltips.forEach(function (tooltip) {
      tooltip.classList.remove('show');
    });
  });
});
