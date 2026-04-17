use anyhow::{Result, bail};

pub struct Detection {
    pub layout: Option<String>,
    pub confidence: f64,
}

fn compute_shannon_entropy(data: &[u8]) -> f64 {
    let mut counts = [0u32; 256];
    for &b in data { counts[b as usize] += 1; }
    let len = data.len() as f64;
    counts.iter().filter(|&&c| c > 0).map(|&c| {
        let p = c as f64 / len;
        -p * p.log2()
    }).sum()
}

pub fn detect_layout(data: &[u8]) -> Detection {
    if data.len() < 32 { return Detection { layout: None, confidence: 0.0 }; }
    let entropy = compute_shannon_entropy(data);
    let mut score = 0.0;
    if data[0x0A] <= 100 { score += 0.4; }
    if entropy > 2.0 && entropy < 7.0 { score += 0.4; }
    if score < 0.7 { return Detection { layout: None, confidence: score }; }
    Detection { layout: Some("IPHONE_11_V1".into()), confidence: score }
}
EOF
echo "✅ Pipeline L8 Desplegado (Esquema WORM + Motor Probabilístico)"