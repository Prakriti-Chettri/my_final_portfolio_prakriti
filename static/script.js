// Fade-in animation fix

const cards = document.querySelectorAll('.card');

window.addEventListener('load', () => {
    cards.forEach(card => {
        card.classList.add('show');
    });
});