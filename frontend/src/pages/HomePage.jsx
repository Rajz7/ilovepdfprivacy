import React from 'react';
import ToolCard from '../components/ToolCard';

const HomePage = () => {
  const tools = [
    { title: 'Merge PDF', description: 'Combine multiple PDFs into one.', path: '/tool/merge-pdf' },
    { title: 'Split PDF', description: 'Extract pages from a PDF.', path: '/tool/split-pdf' },
    { title: 'Compress PDF', description: 'Reduce the file size of your PDF.', path: '/tool/compress-pdf' },
    { title: 'Word to PDF', description: 'Convert Word documents to PDF.', path: '/tool/word-to-pdf' },
    { title: 'Powerpoint to PDF', description: 'Convert Powerpoint presentations to PDF.', path: '/tool/powerpoint-to-pdf' },
    { title: 'Image to PDF', description: 'Convert images to PDF.', path: '/tool/image-to-pdf' },
  ];

  return (
    <div className="relative min-h-screen overflow-hidden px-4 py-8 md:px-8 md:py-10">
      <div className="aurora-orb left-[-140px] top-[-120px] h-80 w-80 bg-cyan-300" />
      <div className="aurora-orb bottom-[-120px] right-[-90px] h-72 w-72 bg-emerald-300" />

      <div className="mx-auto max-w-6xl">
        <header className="appear-up rounded-3xl border border-slate-200/70 bg-white/70 p-6 shadow-[0_24px_60px_-40px_rgba(15,23,42,0.45)] backdrop-blur-xl md:p-10" style={{ animationDelay: '80ms' }}>
          <div className="flex flex-col gap-7">
            <div className="inline-flex w-fit items-center gap-2 rounded-full border border-teal-200 bg-teal-50 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-teal-700">
              Privacy-first PDF workspace
            </div>

            <div className="max-w-3xl">
              <h1 className="font-display text-4xl font-semibold leading-tight tracking-tight text-slate-900 md:text-6xl">
                Beautiful PDF tools.
                <span className="block bg-gradient-to-r from-teal-700 via-cyan-600 to-blue-700 bg-clip-text text-transparent">
                  Zero cloud exposure.
                </span>
              </h1>
              <p className="mt-5 max-w-2xl text-base leading-relaxed text-slate-600 md:text-xl">
                iLovePDFPrivacy gives you a calm, fast workspace for merge, split, compress, and convert operations while your documents stay on your machine.
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-3 text-sm text-slate-600">
              <span className="rounded-full border border-slate-200 bg-white/80 px-3 py-1.5">Local processing only</span>
              <span className="rounded-full border border-slate-200 bg-white/80 px-3 py-1.5">No account required</span>
              <span className="rounded-full border border-slate-200 bg-white/80 px-3 py-1.5">Built for daily workflows</span>
            </div>
          </div>
        </header>

        <section className="mt-8 appear-up" style={{ animationDelay: '180ms' }}>
          <div className="mb-5 flex flex-col gap-2 md:flex-row md:items-end md:justify-between">
            <div>
              <h2 className="font-display text-2xl font-semibold text-slate-900 md:text-3xl">Pick a tool and start in seconds</h2>
              <p className="mt-1 text-sm text-slate-600 md:text-base">A focused set of file operations with predictable, private output.</p>
            </div>
            <p className="text-xs font-semibold uppercase tracking-[0.16em] text-slate-500">6 core actions</p>
          </div>

          <main className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {tools.map((tool, index) => (
              <ToolCard
                key={tool.title}
                title={tool.title}
                description={tool.description}
                path={tool.path}
                index={index}
              />
            ))}
          </main>
        </section>

        <footer className="mt-12 appear-up text-center text-sm text-slate-500" style={{ animationDelay: '260ms' }}>
          Crafted for teams and individuals who want utility with restraint.
        </footer>
      </div>
    </div>
  );
};

export default HomePage;
