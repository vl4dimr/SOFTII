import { useState } from "react";

const escuelas = [
  "Ingenieria de Sistemas",
  "Ingenieria Estadistica e Informatica",
  "Ingenieria Civil",
  "Ingenieria Mecanica Electrica",
  "Ingenieria de Minas",
  "Ingenieria Quimica",
  "Ingenieria Agronomica",
  "Medicina Humana",
  "Derecho",
  "Contabilidad",
  "Administracion",
  "Educacion",
];

export default function TesisForm({ tesis, onSubmit, onClose }) {
  const [titulo, setTitulo] = useState(tesis?.titulo || "");
  const [autor, setAutor] = useState(tesis?.autor || "");
  const [escuela, setEscuela] = useState(
    tesis?.escuela || "Ingenieria de Sistemas"
  );
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({ titulo, autor, escuela });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg animate-fadeIn">
        <div className="p-6 border-b border-gray-100">
          <h2 className="text-xl font-bold text-gray-800">
            {tesis ? "Editar Tesis" : "Nueva Tesis"}
          </h2>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-5">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Titulo
            </label>
            <input
              type="text"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              required
              minLength={10}
              maxLength={500}
              className="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
              placeholder="Titulo de la tesis (min. 10 caracteres)"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Autor
            </label>
            <input
              type="text"
              value={autor}
              onChange={(e) => setAutor(e.target.value)}
              required
              minLength={3}
              maxLength={200}
              className="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition"
              placeholder="Nombre del autor"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Escuela Profesional
            </label>
            <select
              value={escuela}
              onChange={(e) => setEscuela(e.target.value)}
              className="w-full px-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition bg-white"
            >
              {escuelas.map((e) => (
                <option key={e} value={e}>
                  {e}
                </option>
              ))}
            </select>
          </div>

          <div className="flex gap-3 pt-2">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2.5 border border-gray-300 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 bg-blue-600 text-white px-4 py-2.5 rounded-lg font-semibold hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading
                ? "Guardando..."
                : tesis
                ? "Actualizar"
                : "Crear Tesis"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
