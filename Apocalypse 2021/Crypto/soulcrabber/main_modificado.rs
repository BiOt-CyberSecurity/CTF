use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;


fn main() -> std::io::Result<()> {
	let mut rng = SrdRng::seed_from_u64(13371337);
	for _ io 0..64{
		print!("{},", rng.gen::<u8>());
	}
	Ok(())
}

