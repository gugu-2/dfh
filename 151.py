    return st_full
if __name__ == "__main__":
    st_code = assemble()
    print(f"Total assembled ST code length: {len(st_code)} characters")
    print(f"Total lines: {len(st_code.splitlines())}")
    
    user_prompt = """You are Lumina's Principal Automation Fellow & Cyber-Physical Systems Chair (V7 Max-Persona: 75+ years veteran).
Generate an ultra-dense, mathematically complete, fully unrolled IEC 61131-3 Structured Text Function Block for automotive fuel cell electric vehicle (FCEV) metallic bipolar plate ultra-thin foil hydroforming, 2D galvo laser micro-welding, and vacuum helium mass spectrometry leak testing cell, multi-channel 2oo3 TMR sensor voting, discrete state-space dynamic model, receding-horizon MPC with projected gradient descent, deterministic finite state machine, and ANSI/ISA-18.2 alarm management.
"""
    bt = chr(96) * 3
    asst_content = f"{bt}iec-st\n{st_code}\n{bt}"
    
    dataset_id = str(uuid.uuid4())[:8]
    dataset = {
        "messages": [
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": asst_content}
        ]
    }
    
    dest_file = f"data/swarm_raw/agent_{dataset_id}.json"
    with open(dest_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2)
        
    print(f"Dataset saved to: {dest_file}")
    
    # Run validation
    from validate_iec import validate_json_file
    errors = validate_json_file(dest_file)
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(" -", e)
    else:
        print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
