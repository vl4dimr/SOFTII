import { useState, useEffect } from "react";
import {
  listarTesis,
  buscarTesis,
  crearTesis,
  actualizarTesis,
  cambiarEstado,
  eliminarTesis,
} from "./api";

const ESTADOS = ["borrador", "revision", "aprobado", "rechazado"];

function App() {
  const [tesisList, setTesisList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [busqueda, setBusqueda] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [editando, setEditando] = useState(null);
  const [toast, setToast] = useState(null);

  const [form, setForm] = useState({
    titulo: "",
    autor: "",
    escuela: "Ingenieria de Sistemas",
  });

  // Cargar tesis al inicio
  useEffect(() => {
    cargar();
  }, []);

  // Toast auto-hide
  useEffect(() => {
    if (toast) {
      const t = setTimeout(() => setToast(null), 3000);
      return () => clearTimeout(t);
    }
  }, [toast]);

  async function cargar() {
    setLoading(true);
    try {
      const data = await listarTesis();
      setTesisList(data);
    } catch (e) {
      notify("Error al conectar con la API", "error");
    }
    setLoading(false);
  }

  async function handleBuscar() {
    if (!busqueda.trim()) return cargar();
    setLoading(true);
    try {
      const data = await buscarTesis(busqueda);
      setTesisList(data);
    } catch (e) {
      notify("Error al buscar", "error");
    }
    setLoading(false);
  }

  function abrirCrear() {
    setEditando(null);
    setForm({ titulo: "", autor: "", escuela: "Ingenieria de Sistemas" });
    setShowForm(true);
  }

  function abrirEditar(tesis) {
    setEditando(tesis.id);
    setForm({
      titulo: tesis.titulo,
      autor: tesis.autor,
      escuela: tesis.escuela || "Ingenieria de Sistemas",
    });
    setShowForm(true);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      if (editando) {
        await actualizarTesis(editando, form);
        notify("Tesis actualizada");
      } else {
        await crearTesis(form);
        notify("Tesis creada");
      }
      setShowForm(false);
      cargar();
    } catch (err) {
      notify(err.message, "error");
    }
  }

  async function handleEstado(id, estado) {
    try {
      await cambiarEstado(id, estado);
      notify(`Estado: ${estado}`);
      cargar();
    } catch (err) {
      notify(err.message, "error");
    }
  }

  async function handleEliminar(id) {
    if (!confirm("Eliminar esta tesis?")) return;
    try {
      await eliminarTesis(id);
      notify("Tesis eliminada");
      cargar();
    } catch (err) {
      notify(err.message, "error");
    }
  }

  function notify(msg, type = "success") {
    setToast({ msg, type });
  }

  // Stats
  const stats = {
    total: tesisList.length,
    borrador: tesisList.filter((t) => t.estado === "borrador").length,
    revision: tesisList.filter((t) => t.estado === "revision").length,
    aprobado: tesisList.filter((t) => t.estado === "aprobado").length,
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Gestor de Tesis UNAP</h1>
        <p>Lab Sesion 3 - FastAPI + PostgreSQL + React</p>
      </header>

      {/* Stats */}
      <div className="stats">
        <div className="stat-card">
          <div className="number">{stats.total}</div>
          <div className="label">Total</div>
        </div>
        <div className="stat-card">
          <div className="number">{stats.borrador}</div>
          <div className="label">Borrador</div>
        </div>
        <div className="stat-card">
          <div className="number">{stats.revision}</div>
          <div className="label">Revision</div>
        </div>
        <div className="stat-card">
          <div className="number">{stats.aprobado}</div>
          <div className="label">Aprobado</div>
        </div>
      </div>

      {/* Toolbar */}
      <div className="toolbar">
        <input
          type="text"
          placeholder="Buscar por titulo..."
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleBuscar()}
        />
        <button className="btn btn-secondary" onClick={handleBuscar}>
          Buscar
        </button>
        <button
          className="btn btn-secondary"
          onClick={() => {
            setBusqueda("");
            cargar();
          }}
        >
          Limpiar
        </button>
        <button className="btn btn-primary" onClick={abrirCrear}>
          + Nueva Tesis
        </button>
      </div>

      {/* List */}
      {loading ? (
        <div className="loading">Cargando...</div>
      ) : tesisList.length === 0 ? (
        <div className="empty">
          <h3>No hay tesis registradas</h3>
          <p>Crea una nueva tesis para comenzar</p>
        </div>
      ) : (
        <div className="tesis-list">
          {tesisList.map((t) => (
            <div key={t.id} className={`tesis-card ${t.estado}`}>
              <div className="top-row">
                <span className="titulo">{t.titulo}</span>
                <span className="id-badge">ID: {t.id}</span>
              </div>
              <div className="meta">
                <span>
                  <strong>Autor:</strong> {t.autor}
                </span>
                <span>
                  <strong>Escuela:</strong> {t.escuela}
                </span>
                <span className={`estado-badge ${t.estado}`}>{t.estado}</span>
              </div>
              <div className="actions">
                <button
                  className="btn btn-primary btn-sm"
                  onClick={() => abrirEditar(t)}
                >
                  Editar
                </button>
                {ESTADOS.filter((e) => e !== t.estado).map((e) => (
                  <button
                    key={e}
                    className="btn btn-secondary btn-sm"
                    onClick={() => handleEstado(t.id, e)}
                  >
                    {e}
                  </button>
                ))}
                <button
                  className="btn btn-danger btn-sm"
                  onClick={() => handleEliminar(t.id)}
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Modal Form */}
      {showForm && (
        <div className="modal-overlay" onClick={() => setShowForm(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h2>{editando ? "Editar Tesis" : "Nueva Tesis"}</h2>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label>Titulo (min 10 caracteres)</label>
                <input
                  type="text"
                  value={form.titulo}
                  onChange={(e) =>
                    setForm({ ...form, titulo: e.target.value })
                  }
                  placeholder="Titulo de la tesis..."
                  required
                  minLength={10}
                />
              </div>
              <div className="form-group">
                <label>Autor (min 3 caracteres)</label>
                <input
                  type="text"
                  value={form.autor}
                  onChange={(e) =>
                    setForm({ ...form, autor: e.target.value })
                  }
                  placeholder="Nombre del autor..."
                  required
                  minLength={3}
                />
              </div>
              <div className="form-group">
                <label>Escuela Profesional</label>
                <select
                  value={form.escuela}
                  onChange={(e) =>
                    setForm({ ...form, escuela: e.target.value })
                  }
                >
                  <option>Ingenieria de Sistemas</option>
                  <option>Ingenieria Estadistica</option>
                  <option>Ingenieria Civil</option>
                  <option>Ingenieria Mecanica Electrica</option>
                  <option>Ingenieria de Minas</option>
                </select>
              </div>
              <div className="form-actions">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowForm(false)}
                >
                  Cancelar
                </button>
                <button type="submit" className="btn btn-success">
                  {editando ? "Guardar Cambios" : "Crear Tesis"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Toast */}
      {toast && <div className={`toast ${toast.type}`}>{toast.msg}</div>}
    </div>
  );
}

export default App;
