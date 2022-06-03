from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

fila = FabricaFila.pega_fila('prioritaria')
fila.atualizafila()
fila.atualizafila()
fila.atualizafila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaResumida('20/03/2025', 1245)))
