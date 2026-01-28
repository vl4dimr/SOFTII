import { descargarDocxUrl } from "../api";

const estadoConfig = {
  borrador: {
    border: "border-l-gray-400",
    badge: "bg-gray-100 text-gray-700",
    label: "Borrador",
  },
  revision: {
    border: "border-l-yellow-400",
    badge: "bg-yellow-100 text-yellow-700",
    label: "En Revision",
  },
  aprobado: {
    border: "border-l-green-400",
    badge: "bg-green-100 text-green-700",
    label: "Aprobado",
  },
  rechazado: {
    border: "border-l-red-400",
    badge: "bg-red-100 text-red-700",
    label: "Rechazado",
  },
};

const siguienteEstado = {
  borrador: "revision",
  revision: "aprobado",
  aprobado: "borrador",
  rechazado: "borrador",
};

export default function TesisCard({
  tesis,
  token,
  onEdit,
  onDelete,
  onChangeEstado,
  onToast,
}) {
  const config = estadoConfig[tesis.estado] || estadoConfig.borrador;

  async function handleDownloadDocx() {
    try {
      const response = await descargarDocxUrl(token, tesis.id);
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `tesis_${tesis.id}_${tesis.autor.replace(/ /g, "_")}.docx`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
      onToast("Documento DOCX descargado");
    } catch (err) {
      onToast(err.message, "error");
    }
  }

  return (
    <div
      className={`bg-white rounded-xl shadow-sm border-l-4 ${config.border} p-5 animate-slideIn hover:shadow-md transition`}
    >
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            <span
              className={`text-xs font-medium px-2.5 py-0.5 rounded-full ${config.badge}`}
            >
              {config.label}
            </span>
            <span className="text-xs text-gray-400">ID: {tesis.id}</span>
          </div>
          <h3 className="text-lg font-semibold text-gray-800 leading-snug">
            {tesis.titulo}
          </h3>
          <p className="text-sm text-gray-500 mt-1">
            {tesis.autor} &middot; {tesis.escuela || "Sin escuela"}
          </p>
        </div>

        <div className="flex flex-wrap gap-2 shrink-0">
          <button
            onClick={onEdit}
            className="px-3 py-1.5 text-sm bg-blue-50 text-blue-600 rounded-lg hover:bg-blue-100 transition font-medium"
          >
            Editar
          </button>
          <button
            onClick={() => onChangeEstado(siguienteEstado[tesis.estado])}
            className="px-3 py-1.5 text-sm bg-yellow-50 text-yellow-700 rounded-lg hover:bg-yellow-100 transition font-medium"
          >
            {tesis.estado === "borrador"
              ? "Enviar a revision"
              : tesis.estado === "revision"
              ? "Aprobar"
              : "Reiniciar"}
          </button>
          <button
            onClick={handleDownloadDocx}
            className="px-3 py-1.5 text-sm bg-indigo-50 text-indigo-600 rounded-lg hover:bg-indigo-100 transition font-medium"
          >
            DOCX
          </button>
          <button
            onClick={onDelete}
            className="px-3 py-1.5 text-sm bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition font-medium"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>
  );
}
