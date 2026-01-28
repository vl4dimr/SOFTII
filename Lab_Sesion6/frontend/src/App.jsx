import { useState, useEffect } from "react";
import { setOnTokenExpired } from "./api";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import Dashboard from "./pages/Dashboard";

export default function App() {
  const [page, setPage] = useState("login");
  const [token, setToken] = useState(null);

  useEffect(() => {
    // Restaurar sesion desde localStorage
    const savedToken = localStorage.getItem("token");
    if (savedToken) {
      setToken(savedToken);
      setPage("dashboard");
    }

    // Configurar callback para token expirado
    setOnTokenExpired(() => {
      handleLogout();
    });
  }, []);

  function handleLogin(newToken) {
    setToken(newToken);
    localStorage.setItem("token", newToken);
    setPage("dashboard");
  }

  function handleLogout() {
    setToken(null);
    localStorage.removeItem("token");
    setPage("login");
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {page === "login" && (
        <LoginPage
          onLogin={handleLogin}
          onGoToRegister={() => setPage("register")}
        />
      )}
      {page === "register" && (
        <RegisterPage
          onRegistered={() => setPage("login")}
          onGoToLogin={() => setPage("login")}
        />
      )}
      {page === "dashboard" && (
        <Dashboard token={token} onLogout={handleLogout} />
      )}
    </div>
  );
}
