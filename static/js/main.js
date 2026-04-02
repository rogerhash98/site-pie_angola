const productsTrack = document.getElementById('products-track');
const prevButton = document.getElementById('products-prev');
const nextButton = document.getElementById('products-next');
const dotButtons = document.querySelectorAll('#products-dots .dot');

if (productsTrack && prevButton && nextButton && dotButtons.length) {
  const getStep = () => {
    const firstCard = productsTrack.querySelector('.product-slide');
    if (!firstCard) return 0;

    const gap = parseFloat(window.getComputedStyle(productsTrack).gap || '0');
    return firstCard.getBoundingClientRect().width + gap;
  };

  const getPage = () => {
    const step = getStep();
    if (!step) return 0;
    return Math.round(productsTrack.scrollLeft / step);
  };

  const setActiveDot = (index) => {
    dotButtons.forEach((dot, dotIndex) => {
      dot.classList.toggle('is-active', dotIndex === index);
    });
  };

  const goToPage = (index) => {
    const step = getStep();
    productsTrack.scrollTo({ left: step * index, behavior: 'smooth' });
    setActiveDot(index);
  };

  nextButton.addEventListener('click', () => {
    const maxIndex = dotButtons.length - 1;
    const nextIndex = Math.min(getPage() + 1, maxIndex);
    goToPage(nextIndex);
  });

  prevButton.addEventListener('click', () => {
    const prevIndex = Math.max(getPage() - 1, 0);
    goToPage(prevIndex);
  });

  dotButtons.forEach((dot) => {
    dot.addEventListener('click', () => {
      const index = Number(dot.dataset.index || 0);
      goToPage(index);
    });
  });

  productsTrack.addEventListener('scroll', () => {
    setActiveDot(Math.min(getPage(), dotButtons.length - 1));
  });

  window.addEventListener('resize', () => {
    goToPage(Math.min(getPage(), dotButtons.length - 1));
  });
}
