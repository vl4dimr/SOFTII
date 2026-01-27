const API = "http://localhost:8000/api/tesis";

export async function listarTesis() {
  const res = await fetch(API);
  if (!res.ok) throw new Error("Error al listar tesis");
  return res.json();
}

export async function buscarTesis(q) {
  const res = await fetch(`${API}/buscar/?q=${encodeURIComponent(q)}`);
  if (!res.ok) throw new Error("Error al buscar");
  return res.json();
}

export async function obtenerTesis(id) {
  const res = await fetch(`${API}/${id}`);
  if (!res.ok) throw new Error("Tesis no encontrada");
  return res.json();
}

export async function crearTesis(datos) {
  const res = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Error al crear tesis");
  }
  return res.json();
}

export async function actualizarTesis(id, datos) {
  const res = await fetch(`${API}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Error al actualizar");
  }
  return res.json();
}

export async function cambiarEstado(id, estado) {
  const res = await fetch(`${API}/${id}/estado?estado=${estado}`, {
    method: "PATCH",
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Error al cambiar estado");
  }
  return res.json();
}

export async function eliminarTesis(id) {
  const res = await fetch(`${API}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Error al eliminar");
  return res.json();
}
