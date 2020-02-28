import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import (TextArea, AnnotationBbox)

def marimekkompt(ssmarkets,ccsss,lowshare,drawshare,marketshare,height,width,showther,marketsize):
    x=0
    y=0
    print(f"{float(marketsize):,.0f}")
    fig,ax = plt.subplots(1,figsize=(width,height))
    ax.axis([0, 1, 0, 1])
    ax.axis('off')
    marketcount=0

    for market in ssmarkets.index:
        h = float(ssmarkets.loc[market])
        #print(f"height'{market}':{h:.0f}")
        competitors = ccsss.loc[market].sort_values(by=['Share'],ascending=False)
        x=0
        other = 0.0
        count=0
        first = True
        ccompetitor=0
        for competitor in competitors.index:
            if ccompetitor == 0:
                marketboxtext = TextArea(f"{market} ({h*100:.0f}%)", minimumdescent=False)
                ab = AnnotationBbox(marketboxtext, (x,y),
                                    xybox=(x,y),
                                    box_alignment=(0., -0.2))
                ax.add_artist(ab)
            if competitor != 'Other':
                w = float(ccsss.loc[market].loc[competitor])
                if (w >=lowshare):
                    #print(f"  width {competitor}:{w:.0f}")
                    #print(f"({w},{h})")
                    if marketcount > 0: #< (len(ssmarkets.index)-1):
                        rect = patches.Rectangle((x,y),w,h,linewidth=1,edgecolor='k',facecolor='none')
                    else:
                        rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='k',facecolor='none')
                    ax.add_patch(rect)
                    rx, ry = rect.get_xy()
                    cx = rx + rect.get_width()/2.0
                    cy = ry + rect.get_height()/2.0
                    if h>=marketshare:
                        if w<=drawshare:
                            if first:
                                if ccompetitor==0:
                                    count=0
                                else:
                                    count=1
                                first=False                    
                            if count % 2 == 1:
                                ax.annotate(f"{competitor}", (rx+0.005, ry+rect.get_height()*0.9), fontsize=8, ha='left', va='top')
                            else:
                                ax.annotate(f"{competitor}", (rx+0.005, ry+rect.get_height()*0.2), fontsize=8, ha='left', va='top')
                            count += 1                    
                        else:        
                            ax.annotate(f"{competitor}", (rx+0.005, ry+rect.get_height()*0.9), fontsize=8, ha='left', va='top')
                        ax.annotate(f"{w*100:.0f}%", (cx, cy), weight='bold', fontsize=8, ha='center', va='center')
                    x += w
                else:
                    other += w
            else:
                other += float(ccsss.loc[market].loc['Other'])
            ccompetitor +=1
                
        #print(x,y)
        if marketcount > 0:
            rect = patches.Rectangle((x,y),other-0.001,h,linewidth=1,edgecolor='k',facecolor='none')
        else:
            rect = patches.Rectangle((x,y),other,h,linewidth=2,edgecolor='k',facecolor='none')
        ax.add_patch(rect)
        rx, ry = rect.get_xy()
        cx = rx + rect.get_width()/2.0
        cy = ry + rect.get_height()/2.0
        if h>=marketshare:
            if first:
                count=0
                first = False
            if showther:
                if count % 2 == 1:
                    ax.annotate(f"Others", (rx+rect.get_width()/1.2, ry+rect.get_height()*0.9), fontsize=8, ha='left', va='top')
                else:
                    ax.annotate(f"Others", (rx+rect.get_width()/1.2, ry+rect.get_height()*0.2), fontsize=8, ha='left', va='top')
            ax.annotate(f"{other*100:.0f}%", (cx, cy), weight='bold', fontsize=8, ha='center', va='center')
        y += h
        marketcount += 1

    plt.show()
    fig.savefig("marimekko.svg")
