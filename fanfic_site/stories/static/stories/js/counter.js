// Live counter for chapter content
document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.getElementById('id_content');
    const counter = document.getElementById('chapter-counter');
    
    if (!textarea || !counter) return;
    
    function updateCount() {
        const text = textarea.value;
        const words = text.trim().length === 0 ? 0 : text.trim().split(/\s+/).length;
        const chars = text.length;
        
        counter.innerHTML = `${words} word${words !== 1 ? 's' : ''} • ${chars} character${chars !== 1 ? 's' : ''}`;
    }
    
    textarea.addEventListener('input', updateCount);
    updateCount(); // Initial count
});