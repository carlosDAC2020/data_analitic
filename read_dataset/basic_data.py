import pandas as pd 



def get_basic_data(df):
    
    #print(" sin registros nulos")
    # Eliminar registros nulos
    #df = df.dropna()
    #print(df.info())
     
    report = {
        "dimensions":df.shape,
        "size": round(df.memory_usage(deep=True).sum() / (1024 ** 2),2),
        "cant_null":df.isnull().any(axis=1).sum(),
        "cant_repeated":df.duplicated().sum(),
        "variables": vars_info(df)
    }

    return report

    
def vars_info(df):
    # variables 
    vars = tuple(df.columns)
    # tipos de variables
    type_vars = []
    for var in vars:
        type_vars.append(str(df[var].dtype))
    
    vars_info = dict(zip(vars, type_vars))

    # Obtener estadísticas generales para columnas de tipo int64 y float64
    est_vars_nums = df.describe().round(3)

    # Almacenar estadísticas numéricas en el diccionario
    est_vars_nums = est_vars_nums.to_dict()
    for v, t in vars_info.items():
        vars_info[v]={"type":t}
        # caracteristicas de variables numericas 
        if t=="int64" or t == "float64":
            vars_info[v].update(est_vars_nums[v])
            # estadisticas a descartar en variables numericas
            aux = ["count","25%","50%","75%"]
            for el in aux:
                vars_info[v].pop(el)
            
        # caractericticas para variables de tipo object
        else:
            try:
                vars_info[v].update({
                    "Unique values":len(df[v].unique()),
                    "character average":round(sum([len(vl) for vl in df[v].unique()]) / len(df[v].unique()),3)
                })
            except TypeError:
                vars_info[v].update({
                    "mull values": True
                })
            
    return vars_info
    


