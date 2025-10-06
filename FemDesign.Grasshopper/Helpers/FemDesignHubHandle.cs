// https://strusoft.com/
using System;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Lightweight handle object that references a specific FemDesignConnectionHub instance.
    /// </summary>
    public class FemDesignHubHandle
    {
        public Guid Id { get; }

        public FemDesignHubHandle(Guid id)
        {
            Id = id;
        }

        public override string ToString()
        {
            return $"FemDesignHubHandle: {Id}";
        }
    }
}