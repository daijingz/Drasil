# Assumptions {#Sec:Assumps}

This section simplifies the original problem and helps in developing the theoretical models by filling in the missing information for the physical system. The assumptions refine the scope by providing more detail.

<div id="assumpTEO"></div>

Thermal-Energy-Only: The only form of energy that is relevant for this problem is thermal energy. All other forms of energy, such as mechanical energy, are assumed to be negligible. (RefBy: [TM:consThermE](./SecTMs.md#TM:consThermE).)

<div id="assumpHTCC"></div>

Heat-Transfer-Coeffs-Constant: All heat transfer coefficients are constant over time. (RefBy: [TM:nwtnCooling](./SecTMs.md#TM:nwtnCooling).)

<div id="assumpCWTAT"></div>

Constant-Water-Temp-Across-Tank: The water in the tank is fully mixed, so the temperature of the water is the same throughout the entire tank. (RefBy: [GD:rocTempSimp](./SecGDs.md#GD:rocTempSimp).)

<div id="assumpDWCoW"></div>

Density-Water-Constant-over-Volume: The density of water has no spatial variation; that is, it is constant over their entire volume. (RefBy: [GD:rocTempSimp](./SecGDs.md#GD:rocTempSimp).)

<div id="assumpSHECoW"></div>

Specific-Heat-Energy-Constant-over-Volume: The specific heat capacity of water has no spatial variation; that is, it is constant over its entire volume. (RefBy: [GD:rocTempSimp](./SecGDs.md#GD:rocTempSimp).)

<div id="assumpLCCCW"></div>

Newton-Law-Convective-Cooling-Coil-Water: Newton's law of convective cooling applies between the heating coil and the water. (RefBy: [GD:htFluxWaterFromCoil](./SecGDs.md#GD:htFluxWaterFromCoil).)

<div id="assumpTHCCoT"></div>

Temp-Heating-Coil-Constant-over-Time: The temperature of the heating coil is constant over time. (RefBy: [GD:htFluxWaterFromCoil](./SecGDs.md#GD:htFluxWaterFromCoil) and [LC:Temperature-Coil-Variable-Over-Day](./SecLCs.md#likeChgTCVOD).)

<div id="assumpTHCCoL"></div>

Temp-Heating-Coil-Constant-over-Length: The temperature of the heating coil does not vary along its length. (RefBy: [LC:Temperature-Coil-Variable-Over-Length](./SecLCs.md#likeChgTCVOL).)

<div id="assumpCTNTD"></div>

Charging-Tank-No-Temp-Discharge: The model only accounts for charging the tank, not discharging. The temperature of the water can only increase, or remain constant; it cannot decrease. This implies that the initial temperature is less than (or equal to) the temperature of the heating coil. (RefBy: [LC:Discharging-Tank](./SecLCs.md#likeChgDT).)

<div id="assumpWAL"></div>

Water-Always-Liquid: The operating temperature range of the system is such that the material (water in this case) is always in liquid state. That is, the temperature will not drop below the melting point temperature of water, or rise above its boiling point temperature. (RefBy: [TM:sensHtE](./SecTMs.md#TM:sensHtE), [IM:heatEInWtr](./SecIMs.md#IM:heatEInWtr), [IM:eBalanceOnWtr](./SecIMs.md#IM:eBalanceOnWtr), and [UC:Water-Fixed-States](./SecUCs.md#unlikeChgWFS).)

<div id="assumpPIT"></div>

Perfect-Insulation-Tank: The tank is perfectly insulated so that there is no heat loss from the tank. (RefBy: [IM:eBalanceOnWtr](./SecIMs.md#IM:eBalanceOnWtr) and [LC:Tank-Lose-Heat](./SecLCs.md#likeChgTLH).)

<div id="assumpNIHGBW"></div>

No-Internal-Heat-Generation-By-Water: No internal heat is generated by the water; therefore, the volumetric heat generation per unit volume is zero. (RefBy: [IM:eBalanceOnWtr](./SecIMs.md#IM:eBalanceOnWtr) and [UC:No-Internal-Heat-Generation](./SecUCs.md#unlikeChgNIHG).)

<div id="assumpAPT"></div>

Atmospheric-Pressure-Tank: The pressure in the tank is atmospheric, so the melting point temperature and boiling point temperature of water are 0\\({{}^{\circ}\text{C}}\\) and 100\\({{}^{\circ}\text{C}}\\), respectively. (RefBy: [IM:heatEInWtr](./SecIMs.md#IM:heatEInWtr).)

<div id="assumpVCN"></div>

Volume-Coil-Negligible: When considering the volume of water in the tank, the volume of the heating coil is assumed to be negligible. (RefBy: [DD:waterVolume_nopcm](./SecDDs.md#DD:waterVolume.nopcm).)
