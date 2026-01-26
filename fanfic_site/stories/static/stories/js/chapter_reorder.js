// Simple drag-and-drop with SortableJS
document.addEventListener('DOMContentLoaded', function() {
    const chapterList = document.getElementById('chapter-list');
    
    if (!chapterList) return;
    
    // Initialize SortableJS
    const sortable = Sortable.create(chapterList, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost'
    });
    
    // Save button
    const saveButton = document.getElementById('save-chapter-order');
    if (saveButton) {
        saveButton.addEventListener('click', function() {
            const items = chapterList.querySelectorAll('.chapter-item');
            const newOrder = [];
            
            items.forEach((item, index) => {
                newOrder.push({
                    id: item.dataset.chapterId,
                    number: index + 1
                });
            });
            
            console.log('Sending data:', newOrder);
            
            // Send to server
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
                    alert('Chapters reordered successfully!');
                    location.reload();
                } else {
                    alert('Error: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(error => {
                console.error('Full error:', error);
                alert('Error reordering chapters');
            });
        });
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