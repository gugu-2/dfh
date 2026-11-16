IF bAlarmH_AcousticAtten THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000008; END_IF;
IF bAlarmH_Unbalance     THEN udiAlarmWord_ISA_H := udiAlarmWord_ISA_H OR 16#00000010; END_IF;
udiAlarmWord_ISA_L := 16#00000000;
IF bAlarmL_Tension     THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000001; END_IF;
IF bAlarmL_MandrelTemp THEN udiAlarmWord_ISA_L := udiAlarmWord_ISA_L OR 16#00000002; END_IF;
udiAlarmWord_ISA_LL := 16#00000000;
IF bAlarmLL_Tension     THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000001; END_IF;
IF bAlarmLL_MandrelTemp THEN udiAlarmWord_ISA_LL := udiAlarmWord_ISA_LL OR 16#00000002; END_IF;
(* Telemetry Bit-Packing: Operating Status Registers *)
udiStatusWord1 := SHL(TO_UDINT(iFSM_State), 24)
                  OR (BOOL_TO_UDINT(bReady) AND 16#00000001)
                  OR (SHL(BOOL_TO_UDINT(bBusy), 1) AND 16#00000002)
                  OR (SHL(BOOL_TO_UDINT(bDone), 2) AND 16#00000004)
                  OR (SHL(BOOL_TO_UDINT(bError), 3) AND 16#00000008);
udiStatusWord2 := (BOOL_TO_UDINT(bTMR_Healthy_Tension) AND 16#00000001)
                  OR (SHL(BOOL_TO_UDINT(bTMR_Healthy_MandrelTemp), 1) AND 16#00000002)
                  OR (SHL(BOOL_TO_UDINT(bTMR_Healthy_SpindleTorque), 2) AND 16#00000004)
                  OR (SHL(BOOL_TO_UDINT(bTMR_Healthy_AcousticAtten), 3) AND 16#00000008);
udiStatusWord3 := (BOOL_TO_UDINT(bCmd_PneumaticTowCutter_Fire) AND 16#00000001)
                  OR (SHL(BOOL_TO_UDINT(bCmd_EmergencySpindleBrake_Trip), 1) AND 16#00000002);
(* Safety Actuator Clamping Interlocks *)
IF udiAlarmWord_ISA_HH <> 0 OR udiAlarmWord_ISA_LL <> 0 OR NOT bEStopCircuit_Healthy THEN
    bError := TRUE;
    udiErrorID := 16#E001;
    eFsmState := 13; (* Trip into Safe Lockout *)
END_IF;
END_FUNCTION_BLOCK
"""
