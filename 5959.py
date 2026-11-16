    udiAlarmWord_ISA_H := 16#00000000;
    IF bAlm1_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000001; END_IF;
    IF bAlm2_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000002; END_IF;
    IF bAlm3_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000004; END_IF;
    IF bAlm5_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000010; END_IF;
    IF bAlm6_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000020; END_IF;
    IF bAlm9_H_Active  THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000100; END_IF;
    IF bAlm10_H_Active THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000200; END_IF;
    udiAlarmWord_ISA_L := 16#00000000;
    IF bAlm1_L_Active THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000001; END_IF;
    IF bAlm3_L_Active THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000004; END_IF;
    IF bAlm5_L_Active THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000010; END_IF;
    IF bAlm7_L_Active THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000040; END_IF;
    udiAlarmWord_ISA_LL := 16#00000000;
    IF bAlm1_LL_Active THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000001; END_IF;
    IF bAlm3_LL_Active THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000004; END_IF;
    IF bAlm4_LL_Active THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000008; END_IF;
    IF bAlm5_LL_Active THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000010; END_IF;
    IF bAlm7_LL_Active THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000040; END_IF;
    (* Telemetry Bit-Packing: Operating Status Words *)
    udiStatusWord1 := SHL(TO_UDINT(iProductionState), 24)
                      OR (BOOL_TO_UDINT(bSystemReady) AND 16#00000001)
                      OR (SHL(BOOL_TO_UDINT(bCycleActive), 1) AND 16#00000002)
                      OR (SHL(BOOL_TO_UDINT(bCycleComplete), 2) AND 16#00000004)
                      OR (SHL(BOOL_TO_UDINT(bBPPQualityPass), 3) AND 16#00000008)
                      OR (SHL(BOOL_TO_UDINT(bBPPQualityReject), 4) AND 16#00000010)
                      OR (SHL(BOOL_TO_UDINT(bEmergencyAborted), 5) AND 16#00000020);
    udiStatusWord2 := (BOOL_TO_UDINT(bLaserShutterOpen) AND 16#00000001)
                      OR (SHL(BOOL_TO_UDINT(bIntensifierPumpRun), 1) AND 16#00000002)
                      OR (SHL(BOOL_TO_UDINT(bVacuumTurboPumpRun), 2) AND 16#00000004);
    udiStatusWord3 := (BOOL_TO_UDINT(bTMR1_Healthy) AND 16#00000001)
                      OR (SHL(BOOL_TO_UDINT(bTMR2_Healthy), 1) AND 16#00000002)
                      OR (SHL(BOOL_TO_UDINT(bTMR3_Healthy), 2) AND 16#00000004)
                      OR (SHL(BOOL_TO_UDINT(bTMR4_Healthy), 3) AND 16#00000008);
    (* Closed-Loop Actuator Safety Clamping *)
    IF udiAlarmWord_ISA_HH <> 0 OR udiAlarmWord_ISA_LL <> 0 OR NOT bEmergencyStopOk OR bEmergencyAborted THEN
        fIntensifierServoSpeedCmd_mms := 0.0;
        fLaserPowerCmd_W := 0.0;
        bLaserShutterOpen := FALSE;
        fIntensifierPressValve_pct := 100.0; (* Fast depressurization *)
        eCurrentState := 13;
    END_IF;
END_FUNCTION_BLOCK
"""
