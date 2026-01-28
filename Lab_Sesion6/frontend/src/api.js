const API_URL = "http://localhost:8001";

let onTokenExpired = null;

export function setOnTokenExpired(callback) {
  onTokenExpired = callback;
}

async function handleResponse(response) {
  if (response.status === 401) {
    if (onTokenExpired) {
      onTokenExpired();
    }
    throw new Error("Sesion expirada. Inicia sesion nuevamente.");
  }
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.detail || `Error ${response.status}`);
  }
  return response.json();
}

function authHeaders(token) {
  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

// --- Auth (sin token) ---

export async function registrar(nombre, email, password) {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, email, password }),
  });
  return handleResponse(response);
}

export async function login(email, password) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return handleResponse(response);
}

// --- Tesis CRUD (con token) ---

export async function listarTesis(token) {
  const response = await fetch(`${API_URL}/api/tesis`, {
    headers: authHeaders(token),
  });
  return handleResponse(response);
}

export async function crearTesis(token, datos) {
  const response = await fetch(`${API_URL}/api/tesis`, {
    method: "POST",
    headers: authHeaders(token),
    body: JSON.stringify(datos),
  });
  return handleResponse(response);
}

export async function actualizarTesis(token, id, datos) {
  const response = await fetch(`${API_URL}/api/tesis/${id}`, {
    method: "PUT",
    headers: authHeaders(token),
    body: JSON.stringify(datos),
  });
  return handleResponse(response);
}

export async function cambiarEstado(token, id, estado) {
  const response = await fetch(
    `${API_URL}/api/tesis/${id}/estado?estado=${estado}`,
    {
      method: "PATCH",
      headers: authHeaders(token),
    }
  );
  return handleResponse(response);
}

export async function eliminarTesis(token, id) {
  const response = await fetch(`${API_URL}/api/tesis/${id}`, {
    method: "DELETE",
    headers: authHeaders(token),
  });
  return handleResponse(response);
}

// --- Documentos DOCX (con token) ---

export async function descargarDocxUrl(token, id) {
  const response = await fetch(`${API_URL}/documentos/tesis/${id}/docx`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (response.status === 401) {
    if (onTokenExpired) onTokenExpired();
    throw new Error("Sesion expirada.");
  }
  if (!response.ok) {
    throw new Error(`Error al descargar DOCX: ${response.status}`);
  }
  return response;
}
