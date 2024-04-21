'''
CONSTANTE = "Variáveis" que não vai mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)'''

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro pasosu do radar 1')
    
if carro_passou_radar1:
    print('Carro pasou no radar 1')
    
if  carro_multado:
    print('Carro multado em radar 1')