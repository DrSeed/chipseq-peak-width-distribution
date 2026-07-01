import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(9)
tf=rng.lognormal(np.log(250),0.4,3000)     # sharp TF peaks
broad=rng.lognormal(np.log(4000),0.5,1500) # broad histone domains
plt.figure(figsize=(8,4))
plt.hist(tf,bins=60,alpha=.7,label="sharp (TF-like)",color="#4c72b0")
plt.hist(broad,bins=60,alpha=.7,label="broad (histone-like)",color="#dd8452")
plt.xscale("log");plt.xlabel("peak width (bp, log)");plt.ylabel("number of peaks")
plt.title("ChIP-seq peak width distribution (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("bimodal: sharp + broad peaks\n");print("ok")