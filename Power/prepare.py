def prepare(blob):
    # aggregation by products
    blob['markets'] = blob['dfu'].groupby( blob['product']).sum()
    # whole market size
    blob["marketsize"]=blob["markets"].sum()
    # markets sorted by ascending shares
    blob["smarkets"] = blob["markets"].sort_values(by=['Share'],ascending=True)
    # percentatge market
    blob["pMarkets"] = blob["smarkets"]/ blob["marketsize"]
    # create the product x share matrix
    blob["cp"]= blob["dfu"].groupby([blob["market"],blob['product']]).agg({'Share': 'sum'})
    # make it a percentage
    blob["cpp"] = blob["cp"].groupby(level=1).apply(lambda x: x / float(x.sum()))
    # sort it
    blob["ppc"] = blob["cpp"].swaplevel(0,1).sort_index()
