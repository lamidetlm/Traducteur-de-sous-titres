// Fonction pour vérifier l'authentification
function checkAuth() {
    const isAuthenticated = localStorage.getItem('isAuthenticated');
    if (!isAuthenticated) {
        window.location.href = 'login.html';
    }
}

// Fonction pour la connexion
async function login(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('users.json');
        const users = await response.json();
        
        const user = users.find(u => u.username === username && u.password === password);
        
        if (user) {
            localStorage.setItem('isAuthenticated', 'true');
            localStorage.setItem('username', username);
            window.location.href = 'index.html';
        } else {
            alert('Identifiants incorrects');
        }
    } catch (error) {
        console.error('Erreur lors de la connexion:', error);
        alert('Erreur lors de la connexion');
    }
}

// Fonction pour la déconnexion
function logout() {
    localStorage.removeItem('isAuthenticated');
    localStorage.removeItem('username');
    window.location.href = 'login.html';
}
