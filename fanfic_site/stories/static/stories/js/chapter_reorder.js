// Simple drag-and-drop with SortableJS
document.addEventListener('DOMContentLoaded', function () {
    const chapterList = document.getElementById('chapter-list');

    if (!chapterList) {
        console.log('Chapter list not found');
        return;
    }

    console.log('Initializing Sortable...');

    // Initialize SortableJS
    const sortable = Sortable.create(chapterList, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost',
        onEnd: function () {
            console.log('Drag ended - saving order...');
            saveOrder();
        }
    });

    console.log('Sortable initialized');

    function saveOrder() {
        console.log('saveOrder function called');
        const items = chapterList.querySelectorAll('.chapter-item');
        const newOrder = [];

        items.forEach((item, index) => {
            newOrder.push({
                id: item.dataset.chapterId,
                number: index + 1
            });
        });

        console.log('Sending data:', newOrder);

        const storyId = chapterList.dataset.storyId;
        fetch(`/story/${storyId}/reorder-chapters/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ chapters: newOrder })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Response from server:', data);
                if (data.success) {
                    // Update the chapter numbers in the UI
                    const items = chapterList.querySelectorAll('.chapter-item');
                    items.forEach((item, index) => {
                        const link = item.querySelector('a');
                        const chapterNumber = index + 1;
                        // Update the link text to reflect new number
                        link.textContent = link.textContent.replace(/Chapter \d+:/, `Chapter ${chapterNumber}:`);
                        // Update the link href
                        const storyId = chapterList.dataset.storyId;
                        link.href = `/${storyId}/chapters/${chapterNumber}/`;
                    });
                    showSuccessMessage();
                } else {
                    alert('Error: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(error => {
                console.error('Full error:', error);
                alert('Error reordering chapters');
            });
    }

    function showSuccessMessage() {
        const feedback = document.createElement('div');
        feedback.textContent = '✓ Order saved';
        feedback.style.cssText = 'position: fixed; top: 80px; right: 20px; background: #28a745; color: white; padding: 10px 20px; border-radius: 5px; z-index: 1000;';
        document.body.appendChild(feedback);
        setTimeout(() => feedback.remove(), 2000);
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}