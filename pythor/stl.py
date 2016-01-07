class PYSTL(object):
    
    def convert_pd_freqstr(df):
    
        freqstr = df.index.freq.freqstr
        freq_interval = freqstr[-1]
        if len(freqstr)>1:
            freq_number = int(freqstr[:-1])
        else:
            freq_number=1
        if freq_interval is 'Y':
            return 1.0/freq_number
        elif freq_interval is 'M':
            return 12.0/freq_number
        elif freq_interval is 'D':
            return 365.0/freq_number


    def decompose(self, ser, np=12):
        from rpy2 import robjects
        from numpy import asarray
        
        r_stl = robjects.r['stl']
        r_ts = robjects.r['ts']
        start = robjects.IntVector([ser.index[0].year, ser.index[0].month, ser.index[0].day])
        freq = convert_pd_freqstr(ser)
        r_ts_data = r_ts(robjects.FloatVector(asarray(ser)), start=start, frequency=freq)
        r_decomposed = r_stl(r_ts_data, freq)
        res_ts = asarray(r_decomposed[0])
        res_ts = pd.DataFrame({"data":data,
                                    "seasonal" : pd.Series(res_ts[:,0],
                                                           index=data.index),
                                   "trend" : pd.Series(res_ts[:,1],
                                                           index=data.index),
                                   "remainder" : pd.Series(res_ts[:,2],
                                                           index=data.index)})
        
        res_ts = res_ts[['data','seasonal','trend','remainder']]
        self.decomposed = res_ts
        return res_ts
    
    def plot(self, **kwargs):
        import matplotlib.pyplot as plt
        ax = self.decomposed.plot(subplots=True, legend=False, **kwargs)
        plt.tight_layout()
        ax[0].set_ylabel("data")
        ax[1].set_ylabel("seasonal")
        ax[2].set_ylabel("trend")
        ax[3].set_ylabel("remainder")
        ax[3].set_xlabel("Time")