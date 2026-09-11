/* Progressive enhancement: the screenshot strip remains scrollable without JS. */
document.querySelectorAll('.screenshots-section').forEach((section) => {
  const track = section.querySelector('.screenshot-track');
  const previous = section.querySelector('.carousel-prev');
  const next = section.querySelector('.carousel-next');
  const counter = section.querySelector('.carousel-count');
  const cards = [...track.querySelectorAll('.screenshot-card')];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const step = () => cards.length > 1 ? cards[1].offsetLeft - cards[0].offsetLeft : cards[0].offsetWidth;
  const update = () => {
    const atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 3;
    previous.disabled = track.scrollLeft < 3;
    next.disabled = atEnd;
    counter.textContent = `${atEnd ? cards.length : Math.min(cards.length, Math.round(track.scrollLeft / step()) + 1)} / ${cards.length}`;
  };
  const move = (direction) => track.scrollBy({ left: direction * step(), behavior: reducedMotion.matches ? 'instant' : 'smooth' });
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  track.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      move(event.key === 'ArrowRight' ? 1 : -1);
    }
  });
  track.addEventListener('scroll', update, { passive: true });
  new ResizeObserver(update).observe(track);
  update();
});
