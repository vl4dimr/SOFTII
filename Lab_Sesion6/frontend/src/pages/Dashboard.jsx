import { useState, useEffect } from "react";
import { listarTesis, crearTesis, actualizarTesis, eliminarTesis, cambiarEstado } from "../api";
import TesisCard from "../components/TesisCard";
import TesisForm from "../components/TesisForm";
import Toast from "../components/Toast";

export default function Dashboard({ token, onLogout }) {
  const [tesisList, setTesisList] = useState([]);
  const [filteredList, setFilteredList] = useState([]);
  const [search, setSearch] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [editingTesis, setEditingTesis] = useState(null);
  const [loading, setLoading] = useState(true);
  const [toast, setToast] = useState(null);

  useEffect(() => {
    cargarTesis();
  }, []);

  useEffect(() => {
    if (search.trim() === "") {
      setFilteredList(tesisList);
    } else {
      setFilteredList(
        tesisList.filter((t) =>
          t.titulo.toLowerCase().includes(search.toLowerCase())
        )
      );
    }
  }, [search, tesisList]);

  async function cargarTesis() {
    try {
      setLoading(true);
      const data = await listarTesis(token);
      setTesisList(data);
    } catch (err) {
      showToast(err.message, "error");
    } finally {
      setLoading(false);
    }
  }

  function showToast(message, type = "success") {
    setToast({ message, type });
  }

  async function handleCreate(datos) {
    try {
      await crearTesis(token, datos);
      showToast("Tesis creada exitosamente");
      setShowForm(false);
      cargarTesis();
    } catch (err) {
      showToast(err.message, "error");
    }
  }

  async function handleUpdate(id, datos) {
    try {
      await actualizarTesis(token, id, datos);
      showToast("Tesis actualizada exitosamente");
      setShowForm(false);
      setEditingTesis(null);
      cargarTesis();
    } catch (err) {
      showToast(err.message, "error");
    }
  }

  async function handleDelete(id) {
    if (!confirm("Eliminar esta tesis?")) return;
    try {
      await eliminarTesis(token, id);
      showToast("Tesis eliminada");
      cargarTesis();
    } catch (err) {
      showToast(err.message, "error");
    }
  }

  async function handleChangeEstado(id, estado) {
    try {
      await cambiarEstado(token, id, estado);
      showToast(`Estado cambiado a "${estado}"`);
      cargarTesis();
    } catch (err) {
      showToast(err.message, "error");
    }
  }

  function handleEdit(tesis) {
    setEditingTesis(tesis);
    setShowForm(true);
  }

  function handleCloseForm() {
    setShowForm(false);
    setEditingTesis(null);
  }

  // Stats
  const stats = {
    total: tesisList.length,
    borrador: tesisList.filter((t) => t.estado === "borrador").length,
    revision: tesisList.filter((t) => t.estado === "revision").length,
    aprobado: tesisList.filter((t) => t.estado === "aprobado").length,
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {toast && (
        <Toast
          message={toast.message}
          type={toast.type}
          onClose={() => setToast(null)}
        />
      )}

      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-800">
              Tesis UNAP
            </h1>
            <p className="text-sm text-gray-500">Sistema de Gestion de Tesis</p>
          </div>
          <button
            onClick={onLogout}
            className="bg-red-500 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-red-600 transition"
          >
            Cerrar Sesion
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6">
        {/* Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          <div className="bg-white rounded-xl p-4 shadow-sm animate-slideUp">
            <p className="text-sm text-gray-500">Total</p>
            <p className="text-3xl font-bold text-gray-800">{stats.total}</p>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-gray-400 animate-slideUp">
            <p className="text-sm text-gray-500">Borrador</p>
            <p className="text-3xl font-bold text-gray-600">{stats.borrador}</p>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-yellow-400 animate-slideUp">
            <p className="text-sm text-gray-500">Revision</p>
            <p className="text-3xl font-bold text-yellow-600">{stats.revision}</p>
          </div>
          <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-green-400 animate-slideUp">
            <p className="text-sm text-gray-500">Aprobado</p>
            <p className="text-3xl font-bold text-green-600">{stats.aprobado}</p>
          </div>
        </div>

        {/* Search + New button */}
        <div className="flex flex-col sm:flex-row gap-3 mb-6">
          <input
            type="text"
            placeholder="Buscar por titulo..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="flex-1 px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition bg-white"
          />
          <button
            onClick={() => {
              setEditingTesis(null);
              setShowForm(true);
            }}
            className="bg-blue-600 text-white px-6 py-2.5 rounded-lg font-semibold hover:bg-blue-700 transition whitespace-nowrap"
          >
            + Nueva Tesis
          </button>
        </div>

        {/* Tesis List */}
        {loading ? (
          <div className="text-center py-12">
            <div className="inline-block w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
            <p className="text-gray-500 mt-3">Cargando tesis...</p>
          </div>
        ) : filteredList.length === 0 ? (
          <div className="text-center py-12 bg-white rounded-xl shadow-sm">
            <p className="text-gray-400 text-lg">
              {search ? "No se encontraron tesis" : "No hay tesis registradas"}
            </p>
            {!search && (
              <button
                onClick={() => setShowForm(true)}
                className="mt-4 text-blue-600 font-semibold hover:underline"
              >
                Crear la primera tesis
              </button>
            )}
          </div>
        ) : (
          <div className="grid gap-4">
            {filteredList.map((tesis) => (
              <TesisCard
                key={tesis.id}
                tesis={tesis}
                token={token}
                onEdit={() => handleEdit(tesis)}
                onDelete={() => handleDelete(tesis.id)}
                onChangeEstado={(estado) =>
                  handleChangeEstado(tesis.id, estado)
                }
                onToast={showToast}
              />
            ))}
          </div>
        )}
      </main>

      {/* Modal Form */}
      {showForm && (
        <TesisForm
          tesis={editingTesis}
          onSubmit={(datos) => {
            if (editingTesis) {
              handleUpdate(editingTesis.id, datos);
            } else {
              handleCreate(datos);
            }
          }}
          onClose={handleCloseForm}
        />
      )}
    </div>
  );
}
