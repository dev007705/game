// Add event listener to each image for displaying in a modal
document.querySelectorAll('.gallery-item img').forEach(item => {
    item.addEventListener('click', event => {
        showModal(item.src, item.alt);
    });
});

// Function to show modal with clicked image
function showModal(src, alt) {
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = `
        <div class="modal-content">
            <span class="close">&times;</span>
            <img src="${src}" alt="${alt}">
        </div>
    `;
    document.body.appendChild(modal);

    // Close modal when clicking on close button
    modal.querySelector('.close').addEventListener('click', () => {
        document.body.removeChild(modal);
    });
}
