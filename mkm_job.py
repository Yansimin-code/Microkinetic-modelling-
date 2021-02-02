from catmap import ReactionModel
from catmap.parsers import TableParser

mkm_file = 'RWGS.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['production_rate','rate_control'] 
model.run()

from catmap import analyze
mm = analyze.MatrixMap(model)
mm.plot_variable = 'rate_control'
mm.log_scale = False
mm.min = -2
mm.max = 2
mm.subplots_adjust_kwargs = {'wspace':0.6,'hspace':0.6}
mm.plot(save='rate_control.pdf')

vm = analyze.VectorMap(model)
vm.plot_variable = 'rate' #tell the model which output to plot
vm.log_scale = True #rates should be plotted on a log-scale
vm.min = 1e-8 #minimum rate to plot
vm.max = 1e5 #maximum rate to plot
vm.plot(save='rate.pdf') #draw the plot and save it as "rate.pdf"

vm.unique_only = False
vm.subplots_adjust_kwargs = {'left':0.1,'right':0.9,'bottom':0.15,'wspace':0.5,'hspace':0.35}
vm.plot(save='all_rates.pdf')
vm.unique_only = True

model.output_variables += ['production_rate', 'forward_rate', 'reverse_rate', 'rate_constant','forward_rate_constant','reverse_rate_constant', 'equilibrium_constant', 'directional_rates', 'free_energy']
model.run()
vm.production_rate_map = model.production_rate_map #attach map
vm.threshold = 1e-8 #do not plot rates below this
vm.plot_variable = 'production_rate'
vm.plot(save='production_rate.pdf')

vm.descriptor_labels = ['H reactivity [eV]', 'O reactivity [eV]']
vm.subplots_adjust_kwargs = {'left':0.1,'right':0.9,'bottom':0.15,'wspace':0.5,'hspace':0.35}
vm.plot(save='pretty_production_rate.pdf')

vm.plot_variable = 'coverage'
vm.log_scale = False
vm.min = 0
vm.max = 1
vm.plot(save='coverage.pdf')

#vm.include_labels = ['C_s']
#vm.plot(save='C_coverage.pdf')

vm.include_labels = ['O_s']
vm.plot(save='O_coverage.pdf')

vm.include_labels = ['OH_s']
vm.plot(save='OH_coverage.pdf')

vm.include_labels = ['H_s']
vm.plot(save='H_coverage.pdf')

#vm.include_labels = ['CH_s']
#vm.plot(save='CH_coverage.pdf')

sa = analyze.ScalingAnalysis(model)
sa.plot(save='scaling.pdf')

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Co'], save='Co_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Fe'], save='Fe_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Pt'], save='Pt_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Pd'], save='Pd_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Ru'], save='Ru_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Rh'], save='Rh_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Ni'], save='Ni_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = False
fig = ma.plot(plot_variants=['Cu'], save='Cu_FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined

model.model_summary()  # generate a LaTeX summary of the model.  Useful for quick debugging.
