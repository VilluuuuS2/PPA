import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
mes=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
economia=[150,400,90,50,10,200,60,30,100,0,0,0]
fig,ax=plt.subplots(figsize=(7,5))
ax.bar(mes,economia,color=['seagreen', 'darkgreen', 'mediumseagreen'])
ax.set_title('Valores economizados',fontsize=18)
plt.savefig('C:/Users/aluno.INTRAVCA/PPA/PPA/graph.png')
plt.show()

