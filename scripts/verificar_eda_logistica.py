"""Reproduz a base preparada e a EDA de logística."""

from pathlib import Path

import nbformat
import pandas as pd
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "02_eda_logistica.ipynb"
PREPARACAO = ROOT / "notebooks" / "01_tratamento_dados.ipynb"
BASE_TRATADA = ROOT / "data" / "processed" / "nps_tratado.csv"
FIGURES = [
    "logistica_correlacoes.png",
    "logistica_detratores_por_atraso.png",
    "logistica_distribuicao_notas_atraso.png",
    "logistica_prazo_tentativas_frete.png",
]


def main():
    base_publicada = pd.read_csv(BASE_TRATADA)
    preparacao = nbformat.read(PREPARACAO, as_version=4)
    nbformat.validate(preparacao)
    NotebookClient(
        preparacao,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT / "notebooks")}},
    ).execute()
    pd.testing.assert_frame_equal(base_publicada, pd.read_csv(BASE_TRATADA))

    notebook = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(notebook)
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
    )
    client.execute()

    for name in FIGURES:
        path = ROOT / "reports" / "figures" / name
        if not path.is_file() or path.stat().st_size < 1000:
            raise RuntimeError(f"Figura ausente ou vazia: {path}")

    print(f"Preparação e EDA de logística validadas: {len(FIGURES)} figuras.")


if __name__ == "__main__":
    main()
