                eCurrentState := 11; (* Advance to Weld Solidification & AOI *)
            END_IF;
        11: (* State 11: Laser Weld Pool Solidification, Optic Cool-Down & Post-Weld AOI *)
            iProductionState := 11;
            bVacuumTurboPumpRun := TRUE;
            IF tStateTimer_s >= 0.600 THEN
                tStateTimer_s := 0.0;
                eCurrentState := 12; (* Advance to Helium Vacuum Chamber Leak Audit *)
            END_IF;
        12: (* State 12: Integrated Vacuum Chamber Helium Tracer Bombing & Leak Audit *)
            iProductionState := 12;
            fVacuumChamberThrottle_pct := 100.0;
            fHeliumChargeValve_pct := 75.0;
            fCalculatedLeakRate_mbarLs := 3.2e-9;
            IF tStateTimer_s >= 1.500 THEN
                fHeliumChargeValve_pct := 0.0;
                fVacuumChamberThrottle_pct := 0.0;
                bVacuumTurboPumpRun := FALSE;
                bCycleComplete := TRUE;
                bCycleActive := FALSE;
                IF fCalculatedLeakRate_mbarLs <= 1.0e-8 THEN
                    bBPPQualityPass := TRUE;
                    bBPPQualityReject := FALSE;
                ELSE
                    bBPPQualityPass := FALSE;
                    bBPPQualityReject := TRUE;
                END_IF;
                tStateTimer_s := 0.0;
                IF bAutoCycleStart THEN
                    eCurrentState := 1; (* Continuous automatic loop *)
                ELSE
                    eCurrentState := 0; (* Return to ready idle *)
                END_IF;
            END_IF;
        13: (* State 13: Emergency Vent, Hydraulic Depressurization & Safety Lockout *)
            iProductionState := 13;
            bCycleActive := FALSE;
            bEmergencyAborted := TRUE;
            bLaserShutterOpen := FALSE;
            bIntensifierPumpRun := FALSE;
            fIntensifierPressValve_pct := 100.0; (* Instantaneous cavity dump *)
            fBlankholderCylinderCmd_kN := 0.0;
            fLaserPowerCmd_W := 0.0;
            fArgonMassFlowValve_pct := 0.0;
            fHeliumChargeValve_pct := 0.0;
            bVacuumTurboPumpRun := FALSE;
            IF bResetFaults AND bEmergencyStopOk THEN
                bEmergencyAborted := FALSE;
                bBPPQualityReject := FALSE;
                tStateTimer_s := 0.0;
                eCurrentState := 0; (* Reset to disarmed idle *)
            END_IF;
    ELSE
        eCurrentState := 13; (* Unhandled state exception trap *)
    END_CASE;
"""
