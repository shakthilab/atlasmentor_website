import Link from 'next/link';

export default function CallToActionBanner() {
  return (
    <div className="relative overflow-hidden bg-gradient-to-r from-[#0B192C] via-[#1E3A8A] to-[#0B192C] rounded-3xl p-8 sm:p-12 text-white shadow-xl my-12 text-center sm:text-left flex flex-col sm:flex-row items-center justify-between gap-8">
      {/* Glow Effects */}
      <div className="absolute top-0 right-0 w-64 h-64 bg-[#DE8017]/20 rounded-full blur-3xl pointer-events-none" />

      <div className="relative max-w-xl z-10">
        <span className="inline-block bg-[#DE8017] text-white text-xs font-extrabold uppercase tracking-wider px-3 py-1 rounded-full mb-3 shadow-md">
          Take The First Step Today
        </span>
        <h3 className="text-2xl sm:text-3xl font-extrabold mb-3 leading-tight">
          Need Help Choosing the Best University?
        </h3>
        <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
          Book a 1-on-1 free counseling session with Dr. Jitesh Kumar & our expert admissions team to find NMC-approved universities matching your budget.
        </p>
      </div>

      <div className="relative z-10 flex flex-col sm:flex-row gap-3 w-full sm:w-auto flex-shrink-0">
        <a
          href="https://atlasmentor.com/#contact-us"
          className="bg-[#DE8017] hover:bg-[#c97112] text-white font-bold text-sm px-6 py-3.5 rounded-xl shadow-lg transition-all duration-300 transform hover:-translate-y-0.5 text-center"
        >
          Book Free Consultation
        </a>
        <Link
          href="/mbbs-university/russia"
          className="bg-white/10 hover:bg-white/20 border border-white/20 text-white font-semibold text-sm px-6 py-3.5 rounded-xl transition-all text-center"
        >
          Explore Universities
        </Link>
      </div>
    </div>
  );
}
